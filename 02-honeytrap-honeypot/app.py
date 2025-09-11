from flask import Flask, request, jsonify
from datetime import datetime

"""
Simple Flask honeypot that simulates a login page.  It records any credential
submissions along with the requester's IP address and user agent.  The logs
can be retrieved via the /logs endpoint in JSON format.  This is intended
solely for educational or demonstration purposes.
"""

app = Flask(__name__)
logs = []

@app.route("/")
def index():
    """Serve a fake login page."""
    return "Honeypot login page", 200

@app.route("/login", methods=["POST"])
def login():
    """Accepts a username and password, logs the attempt, and always fails."""
    username = request.form.get("username")
    password = request.form.get("password")
    logs.append({
        "timestamp": datetime.utcnow().isoformat(),
        "ip": request.remote_addr,
        "username": username,
        "password": password,
        "user_agent": request.headers.get("User-Agent"),
    })
    return "Invalid credentials", 401

@app.route("/logs", methods=["GET"])
def get_logs():
    """Return the captured credential attempts as JSON."""
    return jsonify(logs)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
