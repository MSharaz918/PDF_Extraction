# 📐 PDF Bounding Box Selector (Streamlit UI)

This tool allows you to **visually select a bounding box** from the first page of a PDF using an OpenCV window and get its coordinates in `(x0, top, x1, bottom)` format—perfect for use with libraries like `pdfplumber`.

---

## 🚀 Features

- Upload a PDF file via browser
- Converts the **first page** to an image
- Launches an OpenCV window to interactively select a bounding box
- Automatically adjusts for large pages (resizing for screen fit)
- Returns coordinates suitable for use with PDF region extractors

---

## 🧩 Requirements

- Python 3.7+
- Poppler installed (required by `pdf2image`)

---

## Install Poppler

- Poppler is required by pdf2image to convert PDF pages to images.

- Windows:

- Download: https://github.com/oschwartz10612/poppler-windows/releases/

- Extract to a directory (e.g., C:\poppler)

- Add C:\poppler\bin to your System PATH environment variable

---

## Install dependencies

- pip install streamlit pdf2image opencv-python

---

## How To Run
- Open cmd
- .venv\Scripts\activate
- streamlit run app.py