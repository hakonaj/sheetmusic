from flask import Flask
from sheetmusic import app

@app.route("/about/")
def about():
    return "<h1>About page</h1>"
