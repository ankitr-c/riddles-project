# from flask import Flask, jsonify
# from flask_cors import CORS
# from pymongo import MongoClient

# app = Flask(__name__)
# CORS(app)

# # for manual container deployement tyr this 
# # client = MongoClient("mongodb://localhost:27017")

# client = MongoClient("mongodb://root:root@127.0.0.1:27017")


# db = client["riddles"]
# collection = db["riddles_collection"]

# @app.route('/get_data', methods=['GET'])
# def get_data():
#     # Fetch data from MongoDB
#     cursor = collection.find({})
#     data = list(cursor)

#     # Convert ObjectId to str for JSON serialization
#     for item in data:
#         item['_id'] = str(item['_id'])
#     print(data)
#     return jsonify(data)

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", debug=True, port=8000)

import flask_cors
from flask import Flask, jsonify, request
import pymongo
from pymongo import MongoClient
import random

app = Flask(__name__)
flask_cors.CORS(app)

# Connect to MongoDB
# client = MongoClient("mongodb://localhost:27017")
client = MongoClient("mongodb://root:root@127.0.0.1:27017")
db = client["your_database_name"]
collection = db["your_collection_name"]

@app.route('/get_riddle', methods=['GET'])
def get_riddle():
    # Retrieve a random riddle from MongoDB
    random_riddle = collection.aggregate([{ '$sample': {'size': 1} }]).next()

    # Return the riddle as JSON
    return jsonify({"riddle": random_riddle["riddle"], "ans": random_riddle["ans"]})

@app.route('/add_riddle', methods=['POST'])
def add_riddle():
    new_riddle = request.json

    # Add the new riddle to MongoDB
    collection.insert_one(new_riddle)

    return jsonify({"message": "Riddle added successfully"})

@app.route('/get_all_riddles', methods=['GET'])
def get_all_riddles():
    all_riddles = list(collection.find({}, {'_id': 0}))
    return jsonify({"riddles": all_riddles})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

