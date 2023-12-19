from flask import Flask, jsonify
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

# for manual container deployement tyr this 
# client = MongoClient("mongodb://localhost:27017")

client = MongoClient("mongodb://root:root@192.168.1.5:27017")


db = client["shopping"]
collection = db["products"]

@app.route('/get_data', methods=['GET'])
def get_data():
    # Fetch data from MongoDB
    cursor = collection.find({})
    data = list(cursor)

    # Convert ObjectId to str for JSON serialization
    for item in data:
        item['_id'] = str(item['_id'])
    print(data)
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8000)
