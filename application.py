import os
import requests
import json

from tkinter import *
from tkinter import messagebox
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from datetime import datetime

from helpers import apology, gardnercal

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    """Buy shares of stock"""
    return render_template("about.html")


@app.route("/project", methods=["GET", "POST"])
def project():
    """Show history of transactions"""
    return render_template("project.html")


@app.route("/project/portfolio")
def portfolio():
    return render_template("portfolio.html")


@app.route("/project/gardner")
def gardner():
    return render_template("gardner.html")

@app.route("/result")
def result():
    try:
        m = int(request.args.get("m"))
        n = int(request.args.get("n"))
        k = int(request.args.get("k"))
    except:
        return apology("Invalid", 400)
    if (m ** k > 10 ** 6):
        return apology("Too big!!", 400)
    x = gardnercal(m, n, k)
    return render_template("result.html", data=x, m=m, n=n, k=k)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    """Show history of transactions"""
    if request.method == "POST":
        url = 'https://notify-api.line.me/api/notify'
        token = 'VfYBJSVwIU5AinCk4fBxXV48SOyl6lYVwkZloLZvI3W'
        headers = {
                    'content-type':
                    'application/x-www-form-urlencoded',
                    'Authorization':'Bearer '+token
                    }
        name = request.form.get("name").strip()
        email = request.form.get("email").strip()
        message = request.form.get("message").strip()
        if not name or not email or not message:
            return render_template("contact.html", status = 0)
        msg = message + '\nFrom: ' + name + '\nEmail: ' + email
        r = requests.post(url, headers=headers , data = {'message':msg})
        print(r.text)
        return render_template("contact.html", status= r.status_code)
    else:
        return render_template("contact.html", status=0)


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
