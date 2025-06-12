# PDF Text Extraction and Visualization 📄🔍

This repository contains four Python scripts designed to automate the extraction and visualization of text from PDF documents. Each script serves a different purpose for extracting text from either the entire document or specific sections, with the ability to visualize certain areas.

## Features 🌟

- **`whole_extract.py`**: Extracts text from the entire PDF document.
- **`section_extract.py`**: Extracts text from a specific section of the PDF using a predefined bounding box.
- **`section_extract_below.py`**: Extracts text from a specific section and also captures the line immediately below the matched keyword.
- **`draw_bounding_box.py`**: Visualizes and draws a bounding box around a specific section of the PDF for area-based extraction.

## Files 📂

1. **`whole_extract.py`**:
   - Extracts text from the entire PDF.
   - Useful for extracting full content without focusing on any particular area.

2. **`section_extract.py`**:
   - Extracts text from a specific area of the PDF using a defined bounding box.
   - Ideal for extracting content from predefined sections like tables or forms.

3. **`section_extract_below.py`**:
   - Similar to `section_extract.py`, but also extracts the line immediately below a keyword match.
   - Useful when you need the context or additional details related to the keyword.

4. **`draw_bounding_box.py`**:
   - Draws a bounding box around a specified area in the PDF.
   - Helps in visualizing the area of interest before extracting text.

## Installation 🛠️

### Prerequisites

- Python 3.x
- Install required libraries with:

```bash
pip install pdfplumber pandas pillow
