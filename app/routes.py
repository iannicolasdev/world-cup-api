from flask import Blueprint, jsonify
from app.services import search_world_cup
from app.data.world_cups import world_cups

bp = Blueprint('api', __name__)

@bp.route("/")
def home():
    return jsonify({"status": "online", "message": "The World Cup API is running!"})

@bp.route("/world-cups")
def all_world_cups():
    return jsonify(world_cups)

@bp.route("/world-cups/<int:edition>")
def search_cup(edition):
    result = search_world_cup(edition)

    if result:
        return jsonify(result)
    
    return jsonify({"error": f"There is no record of a World Cup in {edition}"}), 404