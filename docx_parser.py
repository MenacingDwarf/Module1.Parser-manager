import docx

def extract_text_from_docx(docx_path):
    doc = docx.Document(docx_path)
    text_l = []
    for paragraph in doc.paragraphs:
        text_l.append(paragraph.text)
    return '\n'.join(text_l)

if __name__ == '__main__':
    print(extract_text_from_docx('docx_1.docx'))