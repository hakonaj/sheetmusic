from flask import Flask
from flask import render_template
from sheetmusic import app

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/")
def landing():
	 return render_template("index.html")