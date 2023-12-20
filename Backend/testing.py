import flask_cors
from flask import Flask, jsonify,request
import random

app = Flask(__name__)
flask_cors.CORS(app)
# Sample riddle and answer data
data = [
    {"riddle": "Riddle 1", "ans": "Answer 1"},
    {"riddle": "Riddle 2", "ans": "Answer 2"},
    {"riddle": "Riddle 3", "ans": "Answer 3"}
]

# Variable to keep track of the last served riddle
last_served_riddle = None

@app.route('/get_riddle', methods=['GET'])
def get_riddle():
    global last_served_riddle

    # Exclude the last served riddle from the available riddles
    available_riddles = [r for r in data if r != last_served_riddle]

    # Get a random riddle from the available riddles
    random_riddle = random.choice(available_riddles)

    # Update the last served riddle
    last_served_riddle = random_riddle

    # Return the riddle as JSON
    return jsonify({"riddle": random_riddle["riddle"], "ans": random_riddle["ans"]})

@app.route('/add_riddle', methods=['POST'])
def add_riddle():
    global data
    new_riddle = request.json

    # Add the new riddle to the data
    data.append(new_riddle)

    return jsonify({"message": "Riddle added successfully"})

@app.route('/get_all_riddles', methods=['GET'])
def get_all_riddles():
    global data
    return jsonify({"riddles": data})

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
