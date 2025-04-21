# tests/test_pymupdf.py
import fitz  # PyMuPDF

def test_pymupdf_extract_text():
    # Sample text document creation (for testing)
    doc = fitz.open()
    page = doc.new_page()  # Create a page
    page.insert_text((72, 72), "Hello, PyMuPDF!")
    doc.save("test.pdf")
    
    # Open the saved document to extract text
    doc = fitz.open("test.pdf")
    extracted_text = doc[0].get_text().strip()  # Strip the newline at the end
    assert extracted_text == "Hello, PyMuPDF!"  # Check if text is extracted correctly
    doc.close()
