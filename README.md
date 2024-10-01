# Optical Character Recognition (OCR) Web Application Prototype

## Objective
This project aims to develop a web-based prototype capable of performing Optical Character Recognition (OCR) on an uploaded image containing text in both Hindi and English. The application also includes a basic keyword search functionality based on the extracted text. The web application is accessible via a live URL.

## How to use
### Step 1: Use the [streamlit application.](https://ocr-document-search-web-application.streamlit.app/)
<img src="https://github.com/user-attachments/assets/896732b2-829b-43d0-b4f1-7c3195f7421b" alt="Remote Image" width="800" height="400">

### Step 2: Drag and drop or upload a file.
<img src="https://github.com/user-attachments/assets/5ad94652-1b87-49fe-b878-b6d73b75fae1" alt="Remote Image" width="800" height="400">

### Step 3: Wait for the download and get a response.
<img src="https://github.com/user-attachments/assets/12ed022a-3eca-4be8-9abb-3d074fccfe6a" alt="Remote Image" width="800" height="600">

## Scope
The assignment focuses on creating a web application that:

- Allows users to upload a single image in common formats (JPEG, PNG, etc.).
- Extract text using OCR.
- Provides keyword search functionality based on the extracted text.
- Is deployed and accessible online.

## Tasks Breakdown
### Task 1: Environment Setup and OCR Implementation
#### Environment Setup:
- Set up a Python environment with the following libraries:
Huggingface Transformers
PyTorch
Streamlit (for the web interface)
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

## Contact
If you have any issues or questions, please get in touch with me at guptakshita210@gmail.com.
 







