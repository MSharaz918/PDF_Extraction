import streamlit as st
from pdf2image import convert_from_bytes
import cv2
import tempfile
import os

# Title
st.title("📐 PDF Bounding Box Selector (Streamlit UI)")

# File upload
uploaded_pdf = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_pdf:
    # Convert PDF to image (first page only)
    st.info("Converting first page to image...")
    images = convert_from_bytes(uploaded_pdf.read(), dpi=200)
    image = images[0]

    # Save temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp_file:
        image_path = tmp_file.name
        image.save(image_path, "PNG")

    # Load with OpenCV
    img = cv2.imread(image_path)  # original image
    img_display = img.copy()

    st.image(img[:, :, ::-1], caption="Page 1 - Select bounding box using OpenCV window", use_column_width=True)

    st.warning("⚠️ Click 'Run ROI Selector' below to launch interactive window (outside browser).")

    if st.button("📏 Run ROI Selector"):
        # Resize image to fit screen height if too large
        max_height = 1000  # max height in pixels for display
        h, w = img.shape[:2]
        scale = 1.0

        if h > max_height:
            scale = max_height / h
            img_resized = cv2.resize(img, (int(w * scale), int(h * scale)))
        else:
            img_resized = img.copy()

        # Launch OpenCV window on resized image
        r = cv2.selectROI("Select ROI (Close window after selection)", img_resized, fromCenter=False, showCrosshair=True)
        cv2.destroyAllWindows()

        # Scale coordinates back to original image size
        x, y, w, h = [int(val / scale) for val in r]

        # Format output as bounding box
        x0 = x
        top = y
        x1 = x + w
        bottom = y + h

        st.success("✅ Bounding Box Selected")
        st.code(f"Bounding Box = ({x0}, {top}, {x1}, {bottom})  # (x0, top, x1, bottom)")

        # Optionally draw the box for preview
        img_box = cv2.rectangle(img_display.copy(), (x0, top), (x1, bottom), (0, 255, 0), 2)
        st.image(img_box[:, :, ::-1], caption="Bounding Box Preview")

    # Clean up temp file
    os.remove(image_path)
