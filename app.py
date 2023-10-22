import re
from datetime import datetime

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Flask!"

@app.route("/index")
@app.route("/index/<name>")
def hello_there(name = None):
    return render_template(
        "index.html",
        name = name,
        date=datetime.now()
    )