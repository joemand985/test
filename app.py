from flask import Flask
from models import comments

@app.route("/")
@app.route('/index')