# Optical Character Recognition (OCR) Web Application Prototype

## Objective
This project aims to develop a web-based prototype capable of performing Optical Character Recognition (OCR) on an uploaded image containing text in both Hindi and English. The application also includes a basic keyword search functionality based on the extracted text. The web application is accessible via a live URL.

## Scope
The assignment focuses on creating a web application that:

- Allows users to upload a single image in common formats (JPEG, PNG, etc.).
- Extracts text using OCR.
- Provides keyword search functionality based on the extracted text.
- Is deployed and accessible online.

## Tasks Breakdown
### Task 1: Environment Setup and OCR Implementation
#### Environment Setup:
- Set up a Python environment with the following libraries:
Huggingface Transformers
PyTorch
Streamlit or Gradio (for the web interface)
-Install any other necessary dependencies for OCR.


#### OCR Model Exploration:
Choose from the following OCR models:
- ColPali: Implementation of the Byaldi library + Huggingface Transformers for Qwen2-VL.
- General OCR Theory (GOT): A 580M end-to-end OCR 2.0 model.


#### OCR Model Integration:
- Implement the chosen OCR model to process a single image containing text in Hindi and English.
- The extracted text should be returned in a structured format such as JSON or plain text.


### Task 2: Web Application Development
#### Web Application:
- Develop a basic web application using either Streamlit or Gradio.
- The application must allow users to:
- Upload an image for OCR processing.
- Display the extracted text from the image.
- Enter keywords to search within the extracted text.
- Display search results, highlighting the matching sections.

### Task 3: Deployment
#### Deployment:
- Deploy the web application on platforms like Streamlit Sharing.
- Ensure the web application is accessible via a public URL.
 
## How to Set Up the Environment Locally
### Prerequisites:
- Python 3.x
-  Tesseract
- PyTorch
- Streamlit 


### Steps:
1. Clone the repository:
```bash
git clone https://github.com/imakshug/OCR_and_Document_Search_Web_Application.git
cd OCR_and_Document_Search_Web_Application
 ```
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```
3. Run the web application: For Streamlit:
```bash
streamlit run ocr_streamlit_app.py
```

## How to use
### Step 1: 

### Step 2:

### Step 3: Wait for the download and get a response.



## Contact
If you have any issues or questions, please contact me at guptakshita210@gmail.com.
 







