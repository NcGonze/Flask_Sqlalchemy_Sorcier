from flask import Blueprint, jsonify, request
from api.controllers.auth_controller import AuthController

auth_bp = Blueprint('auth_bp', __name__)
controller = AuthController()


@auth_bp.route("/login", methods=["POST"])
def login():
    try:
        payload = request.get_json(silent=True)
        if not isinstance(payload, dict):
            return jsonify({"error": "JSON body required"}), 400

        data = controller.match_login(payload)
        if data is None:
            return jsonify({"error": "Invalid email or password"}), 401

        return jsonify({"data": data}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
