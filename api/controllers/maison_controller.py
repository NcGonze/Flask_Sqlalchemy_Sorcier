from typing import Any

from api.schemas.maison_schema import MaisonCreateDTO
from dal.repositories.maison_repository import MaisonRepository


class MaisonController:

    def __init__(self):
        self.repo = MaisonRepository()

    def get_all(self):
        try:
            data = self.repo.get_data()
            return data
        except Exception as e:
            print(f"Une erreur est survenue : {e}")

    def create(self, payload: dict[str, Any]):
        if not payload:
            raise ValueError("Payload invalid")

        maison_data = MaisonCreateDTO(**payload)
        return self.repo.create(self._model_to_dict(maison_data))

    @staticmethod
    def _model_to_dict(model):
        if hasattr(model, "model_dump"):
            return model.model_dump(exclude_unset=True)
        return model.dict(exclude_unset=True)
