from app import app
from flask import render_template, request
from app.models import model

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/sendDistrict', methods = ['GET','POST'])
def handleDistrict:
    if request.method=="GET":
        return "You came from the wrong place, go back."
    else: #method is POST
        return "District stuff using Aankit's model."
