from flask import Blueprint, jsonify, request

from api.controllers.exam_controller import ExamenController


exam_bp = Blueprint("exam_bp", __name__, url_prefix="/api/exam")
controller = ExamenController()

@exam_bp.route("/<int:exam_id>", methods=["POST"])
def result_exam(exam_id):
    payload = request.get_json(silent=True)
    result = controller.result_exam(exam_id, payload)
    return jsonify(result)