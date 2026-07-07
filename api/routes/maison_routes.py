from flask import Blueprint, jsonify, request

from api.controllers.maison_controller import MaisonController


maisons_bp = Blueprint("maisons_bp", __name__, url_prefix="/api/maison")
controller = MaisonController()


@maisons_bp.route("/", methods=["GET"])
def get_all_maison():
    try:
        data = controller.get_all()
        return jsonify({
            "data": data,
            "count": len(data),  # type: ignore
        }), 200
    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


@maisons_bp.route("/", methods=["POST"])
def create_maison():
    try:
        payload = request.get_json(silent=True)
        if not isinstance(payload, dict):
            return jsonify({"error": "JSON body required"}), 400

        data = controller.create(payload)
        return jsonify({"data": data}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
