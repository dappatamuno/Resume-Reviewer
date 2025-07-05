import fitz  # PyMuPDF
import docx

def parse_pdf(file):
    text = ""
    with fitz.open(stream=file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text

def parse_docx(file):
    doc = docx.Document(file)
    return "\n".join([p.text for p in doc.paragraphs])

def parse_resume(uploaded_file):
    if uploaded_file.name.endswith(".pdf"):
        return parse_pdf(uploaded_file)
    elif uploaded_file.name.endswith(".docx"):
        return parse_docx(uploaded_file)
    else:
        return ""