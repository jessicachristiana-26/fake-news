import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

# --- 1. Siapkan dataset sederhana ---
# Kalau kamu punya dataset asli, ganti bagian ini dengan pd.read_csv("dataset.csv")
data = pd.DataFrame({
    "text": [
        "Pemerintah mengumumkan vaksin berhasil menurunkan angka kematian.",
        "NASA mengonfirmasi bahwa bumi berbentuk datar.",
        "WHO menyarankan masyarakat menjaga jarak untuk mencegah penyebaran virus.",
        "Bumi hanya sejajar dengan matahari karena konspirasi global."
    ],
    "label": ["real", "fake", "real", "fake"]
})

# --- 2. Preprocessing sederhana ---
X = data["text"]
y = data["label"]

# --- 3. TF-IDF Vectorizer ---
vectorizer = TfidfVectorizer(max_features=5000)
X_vec = vectorizer.fit_transform(X)

# --- 4. Split dan train model ---
X_train, X_test, y_train, y_test = train_test_split(X_vec, y, test_size=0.2, random_state=42)
model = LogisticRegression()
model.fit(X_train, y_train)

# --- 5. Simpan model dan vectorizer ---
joblib.dump(model, "fake_news_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("Model training selesai dan file tersimpan!")
