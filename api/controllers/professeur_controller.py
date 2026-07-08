from typing import Any

from api.schemas.professeur_schema import ProfesseurCreateDTO, ProfesseurUpdateDTO
from dal.repositories.professeur_repository import ProfesseurRepository


class ProfesseurController:

    def __init__(self):
        self.repo = ProfesseurRepository()

    def get_all(self):
        return self.repo.get_all()

    def get_by_id(self, professeur_id: int):
        return self.repo.get_by_id(professeur_id)

    def create(self, payload: dict[str, Any]):
        if not payload:
            raise ValueError("Payload invalid")

        professeur_data = ProfesseurCreateDTO(**payload)
        return self.repo.create(self._model_to_dict(professeur_data))

    def update(self, professeur_id: int, payload: dict[str, Any]):
        if not payload:
            raise ValueError("Payload invalid")

        professeur_data = ProfesseurUpdateDTO(**payload)
        return self.repo.update(professeur_id, self._model_to_dict(professeur_data))

    def delete(self, professeur_id: int):
        return self.repo.delete(professeur_id)

    @staticmethod
    def _model_to_dict(model):
        if hasattr(model, "model_dump"):
            return model.model_dump(exclude_unset=True)
        return model.dict(exclude_unset=True)
