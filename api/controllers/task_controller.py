from dal.repositories.task_repository import TaskRepository
from typing import Any, Optional
from api.schemas.task_schema import TaskFilterDTO, TaskCreateDTO, TaskUpdateDTO


class TaskController:

    def __init__(self):
        self.repo = TaskRepository()

    def get_all(self, task_filter: Optional[TaskFilterDTO] = None):
        done_filter = task_filter.done if task_filter else None
        return self.repo.get_all(done_filter)

    def get_by_id(self, task_id: int):
        return self.repo.get_by_id(task_id)

    def create(self, payload: dict[str, Any]):
        if not payload:
            raise ValueError("Payload invalid")

        task_data = TaskCreateDTO(**payload)
        return self.repo.create(self._model_to_dict(task_data))

    def update(self, task_id: int, payload: dict[str, Any]):
        if not payload:
            raise ValueError("Payload invalid")

        task_data = TaskUpdateDTO(**payload)
        return self.repo.update(task_id, self._model_to_dict(task_data))

    def delete(self, task_id: int):
        return self.repo.delete(task_id)

    @staticmethod
    def _model_to_dict(model):
        if hasattr(model, "model_dump"):
            return model.model_dump(exclude_unset=True)
        return model.dict(exclude_unset=True)
