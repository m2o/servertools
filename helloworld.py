#!/usr/bin/python
import os

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World from %s!" % (os.environ.get('HOSTNAME','?'),)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080)
