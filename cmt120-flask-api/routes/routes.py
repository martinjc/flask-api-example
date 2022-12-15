from kennel import app, db
from models import *

from flask import render_template


@app.route("/")
def index():
    puppies = Puppy.query.all()
    numPuppies = len(puppies)
    return render_template("index.html", numPuppies=numPuppies)
