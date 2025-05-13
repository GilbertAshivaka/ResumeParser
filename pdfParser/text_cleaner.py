import re 

import nltk

try:
    nltk.data.find("corpora/stopwords")

except:
    nltk.download("stopwords")


def clean_text(raw_text: str) -> str:
    text = raw_text.lower()

    #removes any non-ASCII characters
    text = text.encode("ascii", "ignore").decode()

    #replace new lines, carriage returns and tabs with spaces
    text = re.sub(r"[\n\r\t]", " ", text)

    #collapse multiple spaces into a single space
    text = re.sub(r"\s+", " ", text)

    #remove all special characters
    text = re.sub(r"[^\w\s.,-]", "", text)

    return text.strip()
