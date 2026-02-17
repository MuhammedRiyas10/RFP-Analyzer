# core/ocr_utils.py

import pytesseract
from pdf2image import convert_from_bytes
import pdfplumber
import io

# Force correct path (safe hackathon approach)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def extract_text_with_ocr(uploaded_file):
    """
    Hybrid extraction:
    1. Try normal PDF text extraction.
    2. If page has no text, fallback to OCR.
    """

    file_bytes = uploaded_file.read()
    text_output = []

    with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
        for i, page in enumerate(pdf.pages):

            extracted_text = page.extract_text()

            if extracted_text and extracted_text.strip():
                text_output.append(extracted_text)
            else:
                # OCR fallback for scanned page
                images = convert_from_bytes(file_bytes)
                ocr_text = pytesseract.image_to_string(images[i])
                text_output.append(ocr_text)

    return "\n".join(text_output)
