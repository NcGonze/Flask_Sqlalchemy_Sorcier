from flask import Blueprint, jsonify, request

from api.controllers.eleve_controller import EleveController


eleves_bp = Blueprint("eleves_bp", __name__, url_prefix="/api/eleves")
controller = EleveController()


@eleves_bp.route("", methods=["GET"], strict_slashes=False)
def get_all_eleves():
    try:
        data = controller.get_all()
        return jsonify({"data": data, "count": len(data)}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@eleves_bp.route("/<int:eleve_id>", methods=["GET"])
def get_eleve(eleve_id):
    try:
        data = controller.get_by_id(eleve_id)
        if data is None:
            return jsonify({"error": "Eleve not found"}), 404
        return jsonify({"data": data}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@eleves_bp.route("", methods=["POST"], strict_slashes=False)
def create_eleve():
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


@eleves_bp.route("/<int:eleve_id>", methods=["PUT"])
def update_eleve(eleve_id):
    try:
        payload = request.get_json(silent=True)
        if not isinstance(payload, dict):
            return jsonify({"error": "JSON body required"}), 400

        data = controller.update(eleve_id, payload)
        if data is None:
            return jsonify({"error": "Eleve not found"}), 404
        return jsonify({"data": data}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@eleves_bp.route("/<int:eleve_id>", methods=["DELETE"])
def delete_eleve(eleve_id):
    try:
        deleted = controller.delete(eleve_id)
        if not deleted:
            return jsonify({"error": "Eleve not found"}), 404
        return jsonify({"message": "Eleve deleted"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
