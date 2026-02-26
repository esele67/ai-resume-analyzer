import PyPDF2
import docx
import os

def read_pdf(file):
    text = ""
    pdf = PyPDF2.PdfReader(file)
    for page in pdf.pages:
        text += page.extract_text() or ""
    return text

def read_docx(file):
    doc = docx.Document(file)
    return "\n".join([p.text for p in doc.paragraphs])

def read_txt(file):
    return file.read().decode("utf-8")

def extract_text(uploaded_file):
    filename = uploaded_file.name.lower()

    if filename.endswith(".pdf"):
        return read_pdf(uploaded_file)

    elif filename.endswith(".docx"):
        return read_docx(uploaded_file)

    elif filename.endswith(".txt"):
        return read_txt(uploaded_file)

    else:
        return "Unsupported file"
