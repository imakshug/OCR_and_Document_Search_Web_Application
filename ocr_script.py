import torch
from transformers import AutoProcessor, AutoModelForVision2Seq
from PIL import Image
import json
import os
import warnings

# Suppress specific warnings if desired
warnings.filterwarnings("ignore", category=FutureWarning)

# Load the model and processor for the Microsoft model
model_name = "microsoft/trocr-base-handwritten"
token = "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"  # Use token instead of use_auth_token

processor = AutoProcessor.from_pretrained(model_name, token=token)
model = AutoModelForVision2Seq.from_pretrained(model_name, token=token)

# Function to run OCR
def perform_ocr(image_path):
    try:
        # Open the image from the path and convert to RGB
        image = Image.open(image_path).convert("RGB")

        # Preprocess the image
        inputs = processor(images=image, return_tensors="pt")

        # Perform inference (OCR)
        with torch.no_grad():
            outputs = model.generate(**inputs, max_new_tokens=1000)

        # Decode the extracted text
        extracted_text = processor.decode(outputs[0], skip_special_tokens=True)

        # Return result as JSON
        result = {"extracted_text": extracted_text}
        return json.dumps(result, ensure_ascii=False)  # Keeps Hindi characters intact

    except Exception as e:
        return json.dumps({"error": str(e)})

if __name__ == "__main__":
    # Provide the image path here
    image_paths = ["images/english_text.jpg", "images/hindi_text.png"]  # Add paths to your images

    # Create output folder if it doesn't exist
    output_folder = "output"
    os.makedirs(output_folder, exist_ok=True)

    for image_path in image_paths:
        # Call the OCR function
        ocr_result = perform_ocr(image_path)

        # Save the result to a JSON file
        output_file_path = os.path.join(output_folder, os.path.basename(image_path) + "_result.json")
        with open(output_file_path, "w", encoding="utf-8") as output_file:
            output_file.write(ocr_result)

        # Print the extracted text or any errors
        print(f"Result for {image_path}: {ocr_result}")
