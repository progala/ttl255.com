import os
from time import time

from flask import Flask, jsonify


startup_time = time()

app = Flask(__name__)

def time_since_start():
    return time() - startup_time


@app.route("/")
def home():
    if time_since_start() < 10:
        return "", 503

    return "Service ready for use.", 200


@app.route("/status")
def status():    
    if time_since_start() < 10:
        status_val = "NOT_READY"        
    else:
        status_val = "READY"
    
    return jsonify({"status": status_val}), 200


if __name__ == "__main__":
    app.run(port=5010, host="0.0.0.0")