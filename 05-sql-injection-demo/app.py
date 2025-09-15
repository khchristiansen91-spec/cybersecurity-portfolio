from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Setup database with unsanitized input for demonstration
DATABASE = "demo.db"

def init_db():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users (username text, password text)")
    c.execute("INSERT OR IGNORE INTO users VALUES ('admin','password123')")
    conn.commit()
    conn.close()

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    # Vulnerable query (unsanitized string formatting)
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"

    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute(query)
    result = c.fetchone()
    conn.close()

    if result:
        return jsonify({"message": "Authentication successful!"})
    else:
        return jsonify({"message": "Authentication failed."}), 401

@app.route('/')
def index():
    return jsonify({"message": "Send a POST request to /login with username and password."})

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
