from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/data', methods=['GET'])
def generate_data():
    message="A long time ago, in a container far, far away... A python script sent this message."
    return jsonify(message)

app.run(host='0.0.0.0', port=5000) 
