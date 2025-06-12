# PDF Extraction and Keyword Search Automation 📄🔍

This repo contains Python scripts to automatically extract and process text from PDF documents. It uses `pdfplumber` to extract content and `Pandas` to store and analyze the results. You can search for specific keywords, visualize extracted areas, and save the results.

## Features 🌟

- **Extract Text from PDFs**: Extracts text from specific regions using bounding boxes.
- **Keyword Search**: Search for keywords in the extracted text.
- **Save Results**: Save keyword matches into an Excel file 📊.
- **Image Visualization**: Visualize the cropped areas with bounding boxes 🖼️.

## Files 📂

1. **`pdf_extraction_with_image.py`**:
   - Extracts text from PDFs and visualizes cropped areas with bounding boxes.
   - Saves cropped areas as images with bounding boxes drawn.

2. **`pdf_keyword_search_to_excel.py`**:
   - Searches for specific keywords in PDFs.
   - Saves results into an Excel file.

3. **`pdf_keyword_search_with_next_line.py`**:
   - Searches for keywords and returns the next line after a match.
   - Saves results in an Excel file.

4. **`pdf_keyword_search_for_custom_keywords.py`**:
   - Searches for user-defined keywords in PDFs.
   - Outputs results into an Excel file.

## Installation 🛠️

### Prerequisites

- Python 3.x
- Install required libraries with:

```bash
pip install pdfplumber pandas pillow
