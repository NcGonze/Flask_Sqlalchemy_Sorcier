from flask import Blueprint, jsonify, request

from api.controllers.cours_controller import CoursController


cours_bp = Blueprint("cours_bp", __name__, url_prefix="/api/cours")
controller = CoursController()


@cours_bp.route("", methods=["GET"], strict_slashes=False)
def get_all_cours():
    try:
        data = controller.get_all()
        return jsonify({"data": data, "count": len(data)}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@cours_bp.route("/<int:cours_id>", methods=["GET"])
def get_cours(cours_id):
    try:
        data = controller.get_by_id(cours_id)
        if data is None:
            return jsonify({"error": "Cours not found"}), 404
        return jsonify({"data": data}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@cours_bp.route("", methods=["POST"], strict_slashes=False)
def create_cours():
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


@cours_bp.route("/<int:cours_id>", methods=["PUT"])
def update_cours(cours_id):
    try:
        payload = request.get_json(silent=True)
        if not isinstance(payload, dict):
            return jsonify({"error": "JSON body required"}), 400

        data = controller.update(cours_id, payload)
        if data is None:
            return jsonify({"error": "Cours not found"}), 404
        return jsonify({"data": data}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500



@cours_bp.route("/<int:cours_id>", methods=["DELETE"])
def delete_cours(cours_id):
    try:
        deleted = controller.delete(cours_id)
        if not deleted:
            return jsonify({"error": "Cours not found"}), 404
        return jsonify({"message": "Cours deleted"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@cours_bp.route("/sign/<int:cours_id>", methods=["PUT"])
def eleve_cours(cours_id):
    try:
        payload = request.get_json(silent = True)
        if not isinstance(payload, dict):
            return jsonify({"error" : "JSON body required"}), 400
        rep = controller.add_student(cours_id, payload)
        if rep is None:
            return jsonify({"error" : "cours not found"}), 404
        return jsonify({"data": rep}), 200
    except Exception as e:
        return jsonify({"error" : str(e)}), 500
    