from flask import Flask
from flask_cors import CORS
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load .env variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# Connect to MongoDB
mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)
db = client['resumeDB']          # Database
resumes = db['resumes']          # Collection

@app.route('/')
def home():
    return "Flask backend with MongoDB is working!"

@app.route('/save', methods=['POST'])
def save_resume():
    # Dummy data to insert
    data = {
        "name": "Anjali",
        "skills": ["Python", "Flask"],
        "score": 88
    }
    result = resumes.insert_one(data)
    return {"inserted_id": str(result.inserted_id)}

if __name__ == '__main__':
    app.run(debug=True)
