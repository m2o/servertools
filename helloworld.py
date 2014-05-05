#!/usr/bin/python
import os
import socket

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World from %s!" % (socket.gethostname(),)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080)
