from pdfParser.pdf_reader import extract_text_from_pdf
from pdfParser.text_cleaner import clean_text
from pdfParser.data_extractor import extract_resume_info

file_path = "GilbertAshivakaResume.pdf"
raw_text = extract_text_from_pdf(file_path)
cleaned_text = clean_text(raw_text)
info = extract_resume_info(cleaned_text)

print("Extracted Info:")
for key, value in info.items():
    print(f"{key.capitalize()}: {value}, \n")


"AIzaSyARSh3HFFuwsPCf5sP_TLUBh2fougaVCUA"