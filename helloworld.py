#!/usr/bin/python
import os
hostname = os.environ.get('HOSTNAME','?')

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World from %s!" % (hostname,)

if __name__ == "__main__":
    app.run(port=8080)
