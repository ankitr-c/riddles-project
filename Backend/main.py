from flask import Flask, jsonify, request
from pymongo import MongoClient
import random
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
client = MongoClient("mongodb://root:root@localhost:27017")
db = client["riddles"]
riddles_collection = db["riddles_collection"]

@app.route('/get_riddle')
def get_riddle():
    pipeline = [{'$sample': {'size': 1}}]
    try:
        random_riddle = riddles_collection.aggregate(pipeline).next()
        return jsonify(random_riddle)
    except StopIteration:
        return jsonify({"msg": "No riddles available"})

@app.route('/add_riddle', methods=['POST'])
def add_riddle():
    try:
        new_riddle = request.json
        riddles_collection.insert_one(new_riddle)
        return jsonify({"msg": "Riddle added successfully"})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/get_all_riddles')
def get_all_riddles():
    try:
        riddles = list(riddles_collection.find())
        return jsonify(riddles)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
