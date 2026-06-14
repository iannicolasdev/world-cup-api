from flask import Flask, jsonify, abort
from database import world_cups

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "status": "online",
        "message": "The World Cup API is running!"
    })


@app.route("/world-cups")
def list_cups():
    return jsonify(world_cups)


@app.route("/world-cups/<int:edition>")
def search_cup(edition):
    for cup in world_cups:
        if cup["edition"] == edition:
            return jsonify(cup)
    return jsonify({"error": f"There is no record of a World Cup in {edition}"}), 404


if __name__ == "__main__":
    app.run()