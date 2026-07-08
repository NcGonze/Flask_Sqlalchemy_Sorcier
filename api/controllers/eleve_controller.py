from typing import Any

from api.schemas.eleve_schema import EleveCreateDTO, EleveUpdateDTO
from dal.repositories.eleve_repository import EleveRepository


class EleveController:

    def __init__(self):
        self.repo = EleveRepository()

    def get_all(self):
        return self.repo.get_all()

    def get_by_id(self, eleve_id: int):
        return self.repo.get_by_id(eleve_id)

    def create(self, payload: dict[str, Any]):
        if not payload:
            raise ValueError("Payload invalid")

        eleve_data = EleveCreateDTO(**payload)
        return self.repo.create(self._model_to_dict(eleve_data))

    def update(self, eleve_id: int, payload: dict[str, Any]):
        if not payload:
            raise ValueError("Payload invalid")

        eleve_data = EleveUpdateDTO(**payload)
        return self.repo.update(eleve_id, self._model_to_dict(eleve_data))

    def delete(self, eleve_id: int):
        return self.repo.delete(eleve_id)

    @staticmethod
    def _model_to_dict(model):
        if hasattr(model, "model_dump"):
            return model.model_dump(exclude_unset=True)
        return model.dict(exclude_unset=True)
