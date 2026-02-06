import pytesseract
from pdf2image import convert_from_bytes

def ocr_extract(file):
    images = convert_from_bytes(file.file.read())
    text = ""

    for img in images:
        text += pytesseract.image_to_string(img)

    return text

