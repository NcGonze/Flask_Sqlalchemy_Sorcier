from dal.database import get_db
from dal.models.task import Task

class TaskRepository:

    def get_all(self, done_filter):
        with get_db() as db:
            query = db.query(Task)
            if done_filter is not None:

                query = query.filter(Task.done == done_filter)
            
            query = query.order_by(Task.id.desc()).all()
            return [self._serialize_task(task) for task in query]

    def get_by_id(self, task_id):
        with get_db() as db:
            task = db.query(Task).filter(Task.id == task_id).first()
            return self._serialize_task(task) if task else None

    def create(self, data):
        with get_db() as db:
            task = Task(**data)
            db.add(task)
            db.flush()
            return self._serialize_task(task)

    def update(self, task_id, data):
        with get_db() as db:
            task = db.query(Task).filter(Task.id == task_id).first()
            if task is None:
                return None

            for field, value in data.items():
                setattr(task, field, value)

            db.flush()
            return self._serialize_task(task)

    def delete(self, task_id):
        with get_db() as db:
            task = db.query(Task).filter(Task.id == task_id).first()
            if task is None:
                return False

            db.delete(task)
            return True

    @staticmethod
    def _serialize_task(task):
        if task is None:
            return None

        return {
            "id": task.id,
            "titre": task.titre,
            "description": task.description,
            "done": task.done,
            "created_at": task.created_at.isoformat(),
            "updated_at": task.updated_at.isoformat(),
        }