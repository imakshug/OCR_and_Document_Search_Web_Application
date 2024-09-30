import streamlit as st
import os
from PIL import Image
import pytesseract

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Set TESSDATA_PREFIX to the Tesseract directory
os.environ['TESSDATA_PREFIX'] = r'C:\Program Files\Tesseract-OCR'

# Title of the app
st.title("OCR Application: Text Extraction")

# File uploader to upload an image
uploaded_file = st.file_uploader("Choose an image file", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Display the uploaded image
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Image", use_column_width=True)

    # Save the uploaded image to 'uploads' directory
    if not os.path.exists('uploads'):
        os.makedirs('uploads')

    image_path = os.path.join('uploads', uploaded_file.name)
    img.save(image_path)

    # Perform OCR using Tesseract
    text = pytesseract.image_to_string(img, lang='eng+hin')

    # Display extracted text
    st.subheader("Extracted Text")
    st.text(text)
