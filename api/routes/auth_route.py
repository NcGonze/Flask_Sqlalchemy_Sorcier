from flask import Blueprint, jsonify, request
from api.controllers.auth_controller import AuthController

auth_bp = Blueprint('auth_bp', __name__)
controller = AuthController()

@auth_bp.route("/login", methods=["GET"]) # type: ignore
def login():
    try:
        payload = request.get_json()
        if isinstance(payload,dict):
            return jsonify({"error" : "mauvais body"}), 400
        controller.match_login(payload)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    
