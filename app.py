import json
from flask import Flask, render_template, request, url_for, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/prediction')
def get_prediction():
    try:
        with open("status.json", "r") as f:
            data = json.load(f)
        return jsonify(data)
    except Exception as e:
        return jsonify({"prediction": "Error reading prediction"}), 500

if __name__ == '__main__':
    app.run(debug=True)