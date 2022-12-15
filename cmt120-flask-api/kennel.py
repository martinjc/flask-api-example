from flask import Flask
from flask import render_template
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///kennel.sqlite"
db = SQLAlchemy(app)

import routes.routes
import routes.puppies
import routes.owners
