# X-Ray-Image-Preprocessing-and-OCR-Pipeline


## Overview
This project provides a complete pipeline for preprocessing X-Ray images, extracting text using OCR, and generating structured JSON outputs. The code implements advanced preprocessing techniques like skew correction, noise removal, and edge detection, ensuring high-quality OCR results. It also visualizes the bounding boxes around detected text regions and normalizes their coordinates for further analysis.

## Key Features
- **Image Preprocessing**: Handles normalization, skew correction, resizing, denoising, and binarization.
- **Bounding Box Visualization**: Annotates text regions on the image for easy validation.
- **OCR Integration**: Utilizes PaddleOCR for text extraction from images.
- **JSON Output**: Generates a structured JSON file with text data, confidence scores, and normalized coordinates.
- **Error Handling**: Robust exception handling for missing or unsupported image formats.
- **Contour Detection**: Highlights child contours for visual aid in text boundary identification.

## Preprocessing Steps
1. **Normalization**: Normalizes the pixel intensity of the image for improved text clarity.
2. **Noise Removal**: Denoises the image using non-local means.
3. **Binarization**: Converts the image to binary format for OCR.
4. **Edge Detection**: Highlights text edges using Canny edge detection.
5. **Contour Detection**: Identifies child contours to refine text boundaries.

## Output
- **Preprocessed Images**: Annotated bounding boxes saved in the output directory.
- **JSON File**: Contains extracted text, bounding boxes, confidence scores, and normalized coordinates.

