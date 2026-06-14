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


if __name__ == "__main__":
    app.run()