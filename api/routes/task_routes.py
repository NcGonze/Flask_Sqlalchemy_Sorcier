from flask import Blueprint, request, jsonify
from api.controllers.task_controller import TaskController
from api.schemas.task_schema import TaskFilterDTO


task_bp = Blueprint("tasks", __name__, url_prefix="/api/tasks")
controller = TaskController()


@task_bp.route("", methods=["GET"])
def get_all_tasks():
    try:
        done_str = request.args.get("done")
        filters = None

        if done_str is not None:
            if done_str.lower() not in ["true", "false"]:
                return jsonify({"error": "done incorrect"}), 400
            result_filter = done_str == "true"
            filters = TaskFilterDTO(done=result_filter)

        data = controller.get_all(filters)
        return jsonify({"data": data, "count": len(data)}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@task_bp.route("/<int:task_id>", methods=["GET"])
def get_task(task_id):
    try:
        data = controller.get_by_id(task_id)
        if data is None:
            return jsonify({"error": "Task not found"}), 404
        return jsonify({"data": data}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@task_bp.route("", methods=["POST"])
def create_task():
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


@task_bp.route("/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    try:
        payload = request.get_json(silent=True)
        if not isinstance(payload, dict):
            return jsonify({"error": "JSON body required"}), 400

        data = controller.update(task_id, payload)
        if data is None:
            return jsonify({"error": "Task not found"}), 404
        return jsonify({"data": data}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@task_bp.route("/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    try:
        deleted = controller.delete(task_id)
        if not deleted:
            return jsonify({"error": "Task not found"}), 404
        return jsonify({"message": "Task deleted"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500