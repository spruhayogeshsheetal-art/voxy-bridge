from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/cognition/evaluate', methods=['POST'])
def evaluate_code():
    data = request.json or {}
    code = data.get('code', '')
    return jsonify({
        "status": "success",
        "received_code": code
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
