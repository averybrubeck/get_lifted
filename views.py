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

@app.route("/signup/", methods=["GET", "POST"])
def signup():
    if request.method == "POST":

        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        email_conrifmation = request.form["email_confirmation"]
        dob = request.form["birthday"]
        gender = request.form["gender"]
        phone = request.form["phone"]
        country = request.form["country"]
        address = request.form["address"]
        city = request.form["city"]
        state = request.form["state"]
        zip_code = request.form["zip"]
        emergency_contact = request.form["emergency_contact_name"]
        emergency_contact_number = request.form["emergency_contact_number"]
        username = request.form["username"]
        password =  request.form["password"]
        confirmation = request.form["password_confirmation"]

        if password == confirmation and email == email_conrifmation:
            return f"<h1>this worked</h1>"
        else: 
            return render_template("signup.html")
    else:
        return render_template("signup.html") 

@app.route("/login/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return render_template("login.html")
    else:
        return render_template("login.html") 