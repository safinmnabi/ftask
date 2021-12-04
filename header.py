from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    headers = request.headers
    auth = headers.get("X-Api-Key")
    if auth == 'asoidewfoef':
        return jsonify({"message": "OK: Authorized"}), 200
    else:
        return jsonify({"message": "ERROR: Unauthorized"}), 401

if __name__ == '__main__':
    app.run()
