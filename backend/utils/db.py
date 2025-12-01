from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["fake_news_db"]
collection = db["predictions"]

def save_result(text, prediction, confidence):
    collection.insert_one({
        "text": text,
        "prediction": prediction,
        "confidence": confidence
    })
