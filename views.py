from flask import Flask, render_template, url_for, redirect, request
from . import app
import sqlalchemy

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form["name"]
        return f"<h1>this worked</h1>"
    else:
        return render_template("login.html") 

app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"  