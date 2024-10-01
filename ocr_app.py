import os
from flask import Flask, request, render_template
from PIL import Image
import pytesseract

app = Flask(__name__)

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update this path

# Set TESSDATA_PREFIX to the Tesseract directory
os.environ['TESSDATA_PREFIX'] = r'C:\Program Files\Tesseract-OCR'

@app.route('/')
def upload_form():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return 'No file uploaded.'

    file = request.files['file']
    if file.filename == '':
        return 'No file selected.'

    # Save the uploaded image
    image_path = os.path.join('uploads', file.filename)
    file.save(image_path)

    # Perform OCR using Tesseract
    text = extract_text(image_path)

    return render_template('result.html', text=text)

def extract_text(image_path):
    # Load the image
    img = Image.open(image_path)
    # Use Tesseract to extract text
    text = pytesseract.image_to_string(img, lang='eng+hin')  # Add language codes for Hindi and English
    return text

if __name__ == "__main__":
    # Ensure uploads directory exists
    os.makedirs('uploads', exist_ok=True)
    app.run(debug=True)
