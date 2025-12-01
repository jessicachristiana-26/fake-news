from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np
from newspaper import Article
from nlp.preprocess import clean_text

app = Flask(__name__)
CORS(app)  # biar frontend (Next.js, HTML, React) bisa akses API kamu

# === LOAD MODEL ===
model = joblib.load('model/fake_news_model.pkl')
vectorizer = joblib.load('model/vectorizer.pkl')

# === LIST KATA-KATA YANG SERING MUNCUL DI BERITA HOAX ===
SUSPICIOUS_KEYWORDS = [
    "heboh", "menggemparkan", "viral", "terbongkar", "wow",
    "gila", "parah", "mengejutkan", "bikin", "gempar"
]


# ============================================================
#  PREDIKSI DARI TEKS
# ============================================================
@app.route('/predict', methods=['POST'])
def predict_text():
    try:
        data = request.get_json()
        text = data.get("text", "")

        if not text:
            return jsonify({"error": "Teks tidak boleh kosong"}), 400

        cleaned = clean_text(text)
        vec = vectorizer.transform([cleaned])
        prediction = model.predict(vec)[0]
        confidence = float(np.max(model.predict_proba(vec)) * 100)

        suspicious_words = [w for w in SUSPICIOUS_KEYWORDS if w in text.lower()]

        return jsonify({
            "prediction": "FAKE / HOAX" if prediction == 1 else "REAL",
            "confidence": round(confidence, 2),
            "suspicious_words": suspicious_words
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ============================================================
#  PREDIKSI DARI LINK (URL)
# ============================================================
@app.route('/predict-link', methods=['POST'])
def predict_from_link():
    try:
        data = request.get_json()
        url = data.get("url", "")

        if not url:
            return jsonify({"error": "URL tidak boleh kosong"}), 400

        article = Article(url)
        article.download()
        article.parse()

        full_text = f"{article.title}. {article.text}"

        cleaned = clean_text(full_text)
        vec = vectorizer.transform([cleaned])
        prediction = model.predict(vec)[0]
        confidence = float(np.max(model.predict_proba(vec)) * 100)

        suspicious_words = [w for w in SUSPICIOUS_KEYWORDS if w in full_text.lower()]

        return jsonify({
            "prediction": "FAKE / HOAX" if prediction == 1 else "REAL",
            "confidence": round(confidence, 2),
            "suspicious_words": suspicious_words
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ============================================================
#  ROUTE UTAMA / HOMEPAGE
# ============================================================
@app.route('/')
def home():
    return """
    <h1>Fake News Detector API</h1>
    <p>API berjalan dengan baik</p>

    <h3>Endpoint yang bisa kamu pakai:</h3>
    <ul>
        <li><b>POST /predict</b> — kirim teks berita</li>
        <li><b>POST /predict-link</b> — kirim link berita</li>
    </ul>

    <p>Tips: Coba kirim request dari Postman / frontend</p>
    """


# ============================================================
#  RUN SERVER
# ============================================================
if __name__ == '__main__':
    app.run(debug=True)
