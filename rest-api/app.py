import os

from flask import Flask, jsonify, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from models import ItemsModel

host = os.environ["POSTGRES_HOST"]
port = os.environ["POSTGRES_PORT"]
username = os.environ["POSTGRES_USER"]
password = os.environ["POSTGRES_PASS"]
database = os.environ["POSTGRES_DB"]

app = Flask(__name__)
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = f"postgresql://{username}:{password}@{host}:{port}/{database}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.route("/items", methods=["GET"])
def handle_items():
    if request.method == "GET":
        items = ItemsModel.query.all()
        return jsonify([item.serialize for item in items])
    else:
        return {"message": "failure"}


@app.route("/items/<item_name>", methods=["GET"])
def handle_item(item_name):
    if request.method == "GET":
        try:
            item = ItemsModel.query.filter_by(name=item_name).first_or_404()
            return jsonify(item.serialize)
        except:
            return jsonify({"error": f"Item {item_name} not found"})
    else:
        return {"message": "Request method not implemented"}


if __name__ == "__main__":
    app.run(debug=True)
