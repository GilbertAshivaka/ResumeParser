import fitz
def extract_text_from_pdf(filepath : str) -> str:
    try :
        doc = fitz.open(filepath)

        full_text = []

        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            text = page.get_text()
            full_text.append(text)

        doc.close()
        return "\n".join(full_text)
    
    except Exception as e:
        print(f"Failed to extract text from pdf: {e}")
        return ""
    


