# X-Ray-Image-Preprocessing-and-OCR-Pipeline

Overview
This project provides a complete pipeline for preprocessing X-Ray images, extracting text using OCR, and generating structured JSON outputs. The code implements advanced preprocessing techniques like skew correction, noise removal, and edge detection, ensuring high-quality OCR results. It also visualizes the bounding boxes around detected text regions and normalizes their coordinates for further analysis.

Key Features
Image Preprocessing: Handles normalization, skew correction, resizing, denoising, and binarization.
Bounding Box Visualization: Annotates text regions on the image for easy validation.
OCR Integration: Utilizes PaddleOCR for text extraction from images.
JSON Output: Generates a structured JSON file with text data, confidence scores, and normalized coordinates.
Error Handling: Robust exception handling for missing or unsupported image formats.
Contour Detection: Highlights child contours for visual aid in text boundary identification.
Dependencies
Python 3.8+
OpenCV
PaddleOCR
Matplotlib
NumPy
Requests
Install the required libraries using:

bash
Copy code
pip install opencv-python paddleocr matplotlib numpy requests
How to Run
Set input (filepath) and output (outputpath) directories for raw X-Ray images.
Update the url for the OCR API (default: localhost at port 5544).
Execute the script to process images and extract text into a JSON file.
Code Explanation
Section 1: X-Ray Image Processing and OCR with API
Purpose: Process a directory of X-Ray images, draw bounding boxes, and normalize coordinates.
Key Steps:
Read images and encode them in base64 for API consumption.
Call an OCR API to extract text and bounding box details.
Normalize bounding box coordinates relative to the image dimensions.
Save the processed image with annotations and generate a JSON file.
Section 2: PaddleOCR Integration
Purpose: Directly use PaddleOCR for text extraction from preprocessed images.
Key Steps:
Load images and perform OCR with PaddleOCR models.
Extract text, bounding box, and confidence scores.
Normalize bounding box coordinates and save structured JSON output.
Section 3: Advanced Preprocessing
Purpose: Enhance image quality for better OCR accuracy.
Key Steps:
Normalization: Standardizes pixel intensity values.
Skew Correction: Aligns text orientation using the minimum area rectangle.
Scaling: Enlarges the image for improved text clarity.
Noise Removal: Denoises the image using non-local means.
Binarization: Converts the image to binary format for OCR.
Edge Detection: Highlights text edges using Canny edge detection.
Contour Detection: Identifies child contours to refine text boundaries.
Output
Preprocessed images with annotated bounding boxes saved in the output directory.
JSON file containing extracted text, bounding boxes, confidence scores, and normalized coordinates.
