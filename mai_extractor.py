from html_parser import info_extract
from pdf_parser import extract_text_from_pdf
from docx_parser import extract_text_from_docx

def get_text(path):
    if path.endswith('.html'):
        text = info_extract(path)
    elif path.endswith('.pdf'):
        text = extract_text_from_pdf(path)
    elif path.endswith('.docx'):
        text = extract_text_from_docx(path)
    return text

if __name__ == '__main__':
    html_t = get_text('articles/576194.html')
    pdf_t = get_text('pdf_1.pdf')
    docx_t = get_text('docx_1.docx')

    print(html_t)
    print(pdf_t)
    print(docx_t)