from kennel import app, db
from models import *

from flask import jsonify, request


@app.route("/puppies", methods=["GET", "POST"])
def puppies():
    if request.method == "GET":
        puppies = Puppy.query.all()
        return jsonify([p.to_json() for p in puppies])
    elif request.method == "POST":
        puppy = Puppy(name=request.json["name"], age=request.json["age"])
        db.session.add(puppy)
        db.session.commit()
        return jsonify(puppy.to_json())


@app.route("/puppies/<puppy_id>", methods=["GET", "PUT", "DELETE"])
def puppy(puppy_id):
    if request.method == "GET":
        puppy = Puppy.query.get_or_404(puppy_id)
        return jsonify(puppy.to_json())
    elif request.method == "PUT":
        puppy = Puppy.query.get_or_404(puppy_id)
        puppy.name = request.json["name"]
        puppy.age = request.json["age"]
        db.session.add(puppy)
        db.session.commit()
        return jsonify(puppy.to_json())
    elif request.method == "DELETE":
        puppy = Puppy.query.get_or_404(puppy_id)
        db.session.delete(puppy)
        db.session.commit()
        return jsonify("")
