from flask import Flask, jsonify, request
import psycopg2
from flask_cors import CORS
# import random

app = Flask(__name__)
CORS(app)

# Replace the connection parameters with your PostgreSQL database details
conn = psycopg2.connect(
    dbname="riddles",
    user="postgres",
    password="root",
    host="192.168.3.3",
    port="5432"
)

# cursor = conn.cursor()

@app.route('/get_riddle')
def get_riddle():
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT riddle, ans FROM riddles_table ORDER BY RANDOM() LIMIT 1;")
        result = cursor.fetchone()
        conn.commit()
        cursor.close()
        if result:
            return jsonify({"riddle": result[0], "ans": result[1]})
        else:
            return jsonify({"msg": "No riddles available"})
    except Exception as e:
        return jsonify({"error": str(e)})
    # finally:
    #     conn.commit()

@app.route('/add_riddle', methods=['POST'])
def add_riddle():
    try:
        new_riddle_data = request.json
        cursor = conn.cursor()
        cursor.execute("INSERT INTO riddles_table (riddle, ans) VALUES (%s, %s);",
                       (new_riddle_data.get('riddle'), new_riddle_data.get('ans')))
        conn.commit()
        cursor.close()
        return jsonify({"msg": "Riddle added successfully"})
    except Exception as e:
        return jsonify({"error": str(e)})
    # finally:
    #     conn.commit()

@app.route('/get_all_riddles')
def get_all_riddles():
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT riddle, ans FROM riddles_table;")
        results = cursor.fetchall()
        riddles_data = [{"riddle": result[0], "ans": result[1]} for result in results]
        conn.commit()
        cursor.close()
        return jsonify(riddles_data)
    except Exception as e:
        return jsonify({"error": str(e)})
    # finally:
    #     conn.commit()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
