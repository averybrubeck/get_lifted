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

        #fix gender dropdown
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        email_conrifmation = request.form["email_confirmation"]
        dob = request.form["birthday"]
        phone = request.form["phone"]
        address = request.form["address"]
        city = request.form["city"]
        zip_code = request.form["zip"]
        emergency_contact = request.form["emergency_contact_name"]
        emergency_contact_number = request.form["emergency_contact_number"]
        username = request.form["username"]
        password =  request.form["password"]
        confirmation = request.form["password_confirmation"]

        if password == confirmation:
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