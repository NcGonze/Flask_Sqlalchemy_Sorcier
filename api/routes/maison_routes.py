from flask import Blueprint, jsonify, request

from api.controllers.maison_controller import MaisonController


maisons_bp = Blueprint("maisons_bp", __name__, url_prefix="/api/maison")
controller = MaisonController()


# HIGHLIGHT: route liste maison compatible avec /api/maison et /api/maison/.
@maisons_bp.route("", methods=["GET"], strict_slashes=False)
def get_all_maison():
    try:
        data = controller.get_all()
        return jsonify({
            "data": data,
            "count": len(data),
        }), 200
    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


# HIGHLIGHT: nouvelle route pour recuperer une maison par id.
@maisons_bp.route("/<int:maison_id>", methods=["GET"])
def get_maison(maison_id):
    try:
        data = controller.get_by_id(maison_id)
        if data is None:
            return jsonify({"error": "Maison not found"}), 404
        return jsonify({"data": data}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# HIGHLIGHT: route creation maison compatible avec /api/maison et /api/maison/.
@maisons_bp.route("", methods=["POST"], strict_slashes=False)
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


# HIGHLIGHT: nouvelle route pour modifier une maison.
@maisons_bp.route("/<int:maison_id>", methods=["PUT"])
def update_maison(maison_id):
    try:
        payload = request.get_json(silent=True)
        if not isinstance(payload, dict):
            return jsonify({"error": "JSON body required"}), 400

        data = controller.update(maison_id, payload)
        if data is None:
            return jsonify({"error": "Maison not found"}), 404
        return jsonify({"data": data}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# HIGHLIGHT: nouvelle route pour supprimer une maison.
@maisons_bp.route("/<int:maison_id>", methods=["DELETE"])
def delete_maison(maison_id):
    try:
        deleted = controller.delete(maison_id)
        if not deleted:
            return jsonify({"error": "Maison not found"}), 404
        return jsonify({"message": "Maison deleted"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
