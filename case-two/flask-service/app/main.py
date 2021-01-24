from flask import Flask,jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    result='Welcome to my app'
    return jsonify(result),200


@app.route("/status")
def other():
    result2=''
    return jsonify(result2),204
