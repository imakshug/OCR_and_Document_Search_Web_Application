import os
import pandas as pd
import numpy as np
from PIL import Image
from transformers import AutoProcessor, AutoModelForVision2Seq
import torch

# Paths
csv_file = "C:/OCR_and_Document_Search_Web_Application/dataset.csv"  # Specify the path to your CSV file
image_dir = "C:/OCR_and_Document_Search_Web_Application/images"  # Directory containing images

def load_image(image_path):
    # Open the image file and convert to RGB
    with Image.open(image_path) as img:
        img = img.convert("RGB")  # Ensure the image is in RGB format
        return img

def preprocess_image(image, target_size=(224, 224)):
    # Resize and normalize the image
    image = image.resize(target_size)  # Resize to the target size
    img_tensor = torch.tensor(np.array(image)).permute(2, 0, 1) / 255.0  # Convert to tensor and normalize
    return img_tensor.float()

def load_custom_dataset(image_dir, csv_file):
    dataset = []  # Initialize dataset list
    df = pd.read_csv(csv_file)

    df.columns = df.columns.str.strip()  # Remove leading/trailing spaces from column names
    df['image_filename'] = df['image_filename'].str.strip()
    df['text_label'] = df['text_label'].str.strip()

    for idx, row in df.iterrows():
        image_path = os.path.join(image_dir, row['image_filename'])
        img = load_image(image_path)  # Load and transform the image
        img_tensor = preprocess_image(img)  # Preprocess the image
        text = row['text_label']
        dataset.append({"pixel_values": img_tensor, "text": text})

    return dataset

# Example usage
dataset = load_custom_dataset(image_dir, csv_file)
print("Loaded Dataset:", dataset)

# Prepare inputs for the model
inputs = {
    'pixel_values': [data['pixel_values'] for data in dataset],  # Collect pixel values
    'labels': [data['text'] for data in dataset]  # Collect labels
}

def preprocess_data(examples):
    images = []
    texts = examples["text"]
    for image_file in examples["image_filename"]:  # Change this to match your DataFrame
        image_path = os.path.join(image_dir, image_file)
        try:
            img = load_image(image_path)
            img_tensor = preprocess_image(img)  # Preprocess the image
            images.append(img_tensor)
        except FileNotFoundError:
            print(f"File not found: {image_path}")
        except OSError as e:
            print(f"OSError for file {image_path}: {e}")

    if not images:
        print("No valid images found for processing.")
        return {}

    inputs = processor(images=images, text=texts, return_tensors="pt", padding=True, truncation=True)
    return inputs

# Load the model and processor for the Microsoft model
model_name = "microsoft/trocr-base-handwritten"
token = "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"

processor = AutoProcessor.from_pretrained(model_name, token=token)
model = AutoModelForVision2Seq.from_pretrained(model_name, token=token)

# Prepare the dataset for training
train_dataset = pd.DataFrame(dataset)  # Convert list of dicts to DataFrame
print("Train Dataset:")
print(train_dataset)

# Preprocess the dataset
train_dataset = train_dataset.apply(preprocess_data, axis=1)

# Training Logic
model.train()
optimizer = torch.optim.AdamW(model.parameters(), lr=5e-5)

for epoch in range(3):
    for i, batch in enumerate(train_dataset):
        inputs = batch
        optimizer.zero_grad()
        
        # Ensure inputs are properly formatted for the model
        outputs = model(**inputs)
        loss = outputs.loss
        loss.backward()
        optimizer.step()

        if i % 10 == 0:  # Print loss every 10 batches
            print(f"Epoch: {epoch}, Batch: {i}, Loss: {loss.item()}")

# Save the trained model
model.save_pretrained("ocr_model")
processor.save_pretrained("ocr_model")
