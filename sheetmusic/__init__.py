from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object(__name__)

import sheetmusic.controllers

