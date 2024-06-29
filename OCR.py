# -*- coding: utf-8 -*-
"""project_final.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1blNFIXVvEnaVGi8YYJQhDVcpI-aG6Dya
"""

!pip install pillow pytesseract pdfplumber pdf2image
!sudo apt-get install tesseract-ocr
!sudo apt-get install tesseract-ocr-ara
!apt-get install -y poppler-utils

'''
pillow: Python Imaging Library (PIL) fork to handle images.
pytesseract: Python wrapper for Google's Tesseract-OCR Engine.
pdfplumber: Library for extracting text and metadata from PDF files.
pdf2image: Library to convert PDF pages to images.
tesseract-ocr: Optical Character Recognition (OCR) engine.
tesseract-ocr-ara: Arabic language support for Tesseract OCR.
poppler-utils: PDF rendering utilities (required by pdf2image).
'''

import pytesseract
import json
from PIL import Image
from pdf2image import convert_from_path
from google.colab import files

'''
pytesseract: Used to perform OCR on images.
json: Used for handling JSON data.
PIL.Image: Image processing from the Python Imaging Library.
pdf2image.convert_from_path: Converts PDF pages to images.
google.colab.files: Handles file uploads in Google Colab environment.
'''

#Performs OCR on a single image and returns the extracted text.
def ocr_image(image):
    text = pytesseract.image_to_string(image, lang='eng+ara')
    return clean_text(text)

#Removes unwanted characters from the extracted text.
def clean_text(text):
    unwanted_chars = ['\ufeff', '\u200c', '\u200e', '\u200f', 'UCF 200']
    for char in unwanted_chars:
        text = text.replace(char, '')
    return text

#Extracts text from PDF images and returns a list of dictionaries containing page numbers and extracted text.
def extract_text_from_pdf_images(pdf_path):
    images = convert_from_path(pdf_path)
    all_text = []
    for page_number, image in enumerate(images, start=1):
        text = ocr_image(image)
        page_data = {"page_number": page_number, "text": text}
        all_text.append(page_data)
    return all_text

#Saves the extracted text to a JSON file.
def save_text_with_layout(extracted_text, output_path):
    with open(output_path, 'w', encoding='utf-8') as file:
        if isinstance(extracted_text, list):
            for page in extracted_text:
                if 'text' in page:
                    file.write(page['text'])
        elif isinstance(extracted_text, str):
            file.write(extracted_text)
        else:
            raise ValueError("Invalid input type for extracted_text. Expected list or str.")

#Handles file upload and returns the uploaded filename.
def handle_file_upload(file_type):
    uploaded = files.upload()
    for filename in uploaded.keys():
        return filename

# Main function to determine file type and process accordingly.
def main(file_path, output_path, file_type):
    if file_type == 'image':
        image = Image.open(file_path)
        extracted_text = ocr_image(image)
        save_text_with_layout(extracted_text, output_path)
    elif file_type == 'pdf':
        extracted_text = extract_text_from_pdf_images(file_path)
        save_text_with_layout(extracted_text, output_path)
    else:
        raise ValueError("Invalid input type. Please choose 'image' or 'pdf'.")

if __name__ == "__main__":
    file_type = input("Enter file type ('image' or 'pdf'): ").lower()
    if file_type not in ['image', 'pdf']:
        raise ValueError("Invalid file type. Please choose 'image' or 'pdf'.")

    input_file = handle_file_upload(file_type)
    output_file = input("Enter output file name (e.g., output.json): ").strip()

    main(input_file, output_file, file_type)

"""# **Converting pdf to text with layout using pdfplumber**"""

'''
Instead of using OCR, we can directly convert PDFs into JSON while maintaining the layout,
as using Tesseract OCR is not yielding equivalent results due to PDFs containing columns

'''

import pdfplumber


def extract_text_with_layout(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        all_text = []
        for page in pdf.pages:
            # Extract text with layout hints
            text = page.extract_text(layout=True)
            all_text.append(text)
    return all_text


def save_text_with_layout(extracted_text, output_path):
    with open(output_path, 'w', encoding='utf-8') as file:
        for page_text in extracted_text:
            if page_text:
                file.write(page_text)

file_path = '/content/E-Invoice.pdf'
extracted_text = extract_text_with_layout(file_path)
save_text_with_layout(extracted_text, "output_pdf.json")

'''
We can train Tesseract with the given layout if we have enough data.
Initially, it could be trained on Ubuntu using Docker, but there is also a GUI for Windows.
For that, we need at least 200 PDFs and their corresponding texts.
'''