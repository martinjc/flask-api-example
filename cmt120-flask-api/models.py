from kennel import db
from flask_sqlalchemy import SQLAlchemy


class Puppy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    age = db.Column(db.Integer)
    owner_id = db.Column(db.Integer, db.ForeignKey("owner.id"))
    owner = db.relationship("Owner", back_populates="puppies")

    def to_json(self):
        return {
            "name": self.name,
            "age": self.age,
            "owner": self.owner_id,
            "id": self.id,
        }


class Owner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    puppies = db.relationship("Puppy", back_populates="owner")

    def to_json(self):
        return {
            "name": self.name,
            "puppies": [{"id": p.id, "name": p.name} for p in self.puppies],
        }


if __name__ == "__main__":

    db.create_all()

    puppy1 = Puppy(name="Bennie", age=1)
    puppy2 = Puppy(name="Maisy", age=1)

    owner1 = Owner(name="Martin")
    owner2 = Owner(name="Steve")

    owner1.puppies.append(puppy1)
    owner2.puppies.append(puppy2)

    db.session.add(puppy1)
    db.session.add(puppy2)
    db.session.add(owner1)
    db.session.add(owner2)

    db.session.commit()
