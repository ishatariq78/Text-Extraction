# Overview

1. OCR Image Function (ocr_image):
    Takes an image file as input and performs OCR to extract text.
    Supports both English and Arabic languages.
2. Clean Text Function (clean_text):
    Removes unwanted characters from the extracted text to ensure clean and readable output.
3. Extract Text from PDF Images Function (extract_text_from_pdf_images):
    Converts each page of a PDF file into images and performs OCR on each image.
    Returns a list of dictionaries containing page numbers and extracted text.
4. Save Text with Layout Function (save_text_with_layout):
    Saves the extracted text to a JSON file, maintaining the layout as much as possible.
5. Handle File Upload Function (handle_file_upload):
    Manages file uploads and returns the uploaded filename.
6. Main Function (main):
    Determines the type of file (image or PDF) and processes it accordingly.
    Utilizes the appropriate extraction function and saves the text output to a specified file.

# Alternative PDF Extraction
The tool also includes a method for directly extracting text from PDFs while preserving the layout, without using OCR:
1. Extract Text with Layout Function (extract_text_with_layout):
    Uses pdfplumber to extract text from PDFs, preserving the layout.
    Suitable for PDFs containing columns and complex formatting.

# Usage
1. Run the tool and specify the type of file (image or PDF).
2. Upload the file using the provided upload function.
3. The tool will process the file and save the extracted text to a JSON file.

# Future Improvements
1. Train Tesseract with custom layouts using a dataset of at least 200 PDFs and their corresponding texts.
2. Consider using Docker for training on Ubuntu or using a GUI for training on Windows.
