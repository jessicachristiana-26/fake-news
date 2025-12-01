import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer

# download stopwords (pertama kali aja)
nltk.download('stopwords')

def clean_text(text):
    """Membersihkan teks dari simbol, URL, dan stopwords"""
    text = text.lower()
    text = re.sub(r"http\S+", "", text)  # hapus URL
    text = re.sub(r"[^a-zA-Z\s]", "", text)  # hapus angka dan simbol
    words = text.split()
    stop_words = set(stopwords.words('english') + stopwords.words('indonesian'))
    stemmer = SnowballStemmer('english')
    words = [stemmer.stem(word) for word in words if word not in stop_words]
    return " ".join(words)
