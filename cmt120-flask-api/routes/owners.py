from kennel import app, db
from models import *

from flask import jsonify, request


@app.route("/owners", methods=["GET", "POST"])
def owners():
    if request.method == "GET":
        owners = Owner.query.all()
        ret = [o.to_json() for o in owners]
        return jsonify(ret)
    elif request.method == "POST":
        owner = Owner(name=request.json["name"])
        db.session.add(owner)
        db.session.commit()
        ret = owner.to_json()
        return jsonify(ret)


@app.route("/owners/<owner_id>", methods=["GET", "PUT", "DELETE"])
def owner(owner_id):
    if request.method == "GET":
        owner = Owner.query.get_or_404(owner)
        return jsonify(owner.to_json())
    elif request.method == "PUT":
        owner = Owner.query.get_or_404(owner_id)
        owner.name = request.json["name"]
        db.session.add(owner)
        db.session.commit()
        return jsonify(owner.to_json())
    elif request.method == "DELETE":
        owner = Owner.query.get_or_404(owner_id)
        db.session.delete(owner)
        db.session.commit()
        return jsonify("")


@app.route("/owners/<owner_id>/puppies", methods=["POST"])
def add_puppy_to_owner(owner_id):
    owner = Owner.query.get_or_404(owner_id)
    puppy = Puppy.query.filter_by(name=request.json["puppyName"]).first()
    if puppy is None:
        puppy = Puppy(name=request.json["puppyName"], age=request.json["puppyAge"])
    owner.puppies.append(puppy)
    db.session.add(puppy)
    db.session.add(owner)
    db.session.commit()
    ret = owner.to_json()
    return jsonify(ret)
