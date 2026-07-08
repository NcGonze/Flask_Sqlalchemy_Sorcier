from typing import Any

from api.schemas.maison_schema import MaisonCreateDTO, MaisonUpdateDTO
from dal.repositories.maison_repository import MaisonRepository


class MaisonController:

    def __init__(self):
        self.repo = MaisonRepository()

    def get_all(self):
        return self.repo.get_all()

    # HIGHLIGHT: lecture d'une maison par son id.
    def get_by_id(self, maison_id: int):
        return self.repo.get_by_id(maison_id)

    def create(self, payload: dict[str, Any]):
        if not payload:
            raise ValueError("Payload invalid")

        maison_data = MaisonCreateDTO(**payload)
        return self.repo.create(self._model_to_dict(maison_data))

    # HIGHLIGHT: modification d'une maison existante.
    def update(self, maison_id: int, payload: dict[str, Any]):
        if not payload:
            raise ValueError("Payload invalid")

        maison_data = MaisonUpdateDTO(**payload)
        return self.repo.update(maison_id, self._model_to_dict(maison_data))

    # HIGHLIGHT: suppression d'une maison.
    def delete(self, maison_id: int):
        return self.repo.delete(maison_id)

    @staticmethod
    def _model_to_dict(model):
        if hasattr(model, "model_dump"):
            return model.model_dump(exclude_unset=True)
        return model.dict(exclude_unset=True)
