%%writefile app.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"status": "success", "message": "Hello, Railway is working!"})

@app.route('/health')
def health():
    return jsonify({"status": "ok", "message": "Server is running!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
