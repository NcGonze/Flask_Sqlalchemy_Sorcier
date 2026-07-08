from flask import Blueprint, jsonify, request

from api.controllers.professeur_controller import ProfesseurController


professeurs_bp = Blueprint("professeurs_bp", __name__, url_prefix="/api/professeurs")
controller = ProfesseurController()


@professeurs_bp.route("", methods=["GET"], strict_slashes=False)
def get_all_professeurs():
    try:
        data = controller.get_all()
        return jsonify({"data": data, "count": len(data)}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@professeurs_bp.route("/<int:professeur_id>", methods=["GET"])
def get_professeur(professeur_id):
    try:
        data = controller.get_by_id(professeur_id)
        if data is None:
            return jsonify({"error": "Professeur not found"}), 404
        return jsonify({"data": data}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@professeurs_bp.route("", methods=["POST"], strict_slashes=False)
def create_professeur():
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


@professeurs_bp.route("/<int:professeur_id>", methods=["PUT"])
def update_professeur(professeur_id):
    try:
        payload = request.get_json(silent=True)
        if not isinstance(payload, dict):
            return jsonify({"error": "JSON body required"}), 400

        data = controller.update(professeur_id, payload)
        if data is None:
            return jsonify({"error": "Professeur not found"}), 404
        return jsonify({"data": data}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@professeurs_bp.route("/<int:professeur_id>", methods=["DELETE"])
def delete_professeur(professeur_id):
    try:
        deleted = controller.delete(professeur_id)
        if not deleted:
            return jsonify({"error": "Professeur not found"}), 404
        return jsonify({"message": "Professeur deleted"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
