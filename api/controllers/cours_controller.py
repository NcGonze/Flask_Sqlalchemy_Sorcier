from typing import Any

from api.schemas.cours_schema import CoursCreateDTO, CoursUpdateDTO
from dal.repositories.cours_repository import CoursRepository


class CoursController:

    def __init__(self):
        self.repo = CoursRepository()

    # HIGHLIGHT: controleur CRUD complet pour les cours.
    def get_all(self):
        return self.repo.get_all()

    def get_by_id(self, cours_id: int):
        return self.repo.get_by_id(cours_id)

    def create(self, payload: dict[str, Any]):
        if not payload:
            raise ValueError("Payload invalid")

        cours_data = CoursCreateDTO(**payload)
        return self.repo.create(self._model_to_dict(cours_data))

    def update(self, cours_id: int, payload: dict[str, Any]):
        if not payload:
            raise ValueError("Payload invalid")

        cours_data = CoursUpdateDTO(**payload)
        return self.repo.update(cours_id, self._model_to_dict(cours_data))

    def delete(self, cours_id: int):
        return self.repo.delete(cours_id)
    
    def add_student(self,cours_id,payload):
        cap, nbre = self.repo.get_capacite(cours_id)
        if nbre >= cap:
            raise ValueError("Capacite max atteinte")
        stud_id = payload.id
        return self.repo.add_eleve(cours_id,stud_id)

    @staticmethod
    def _model_to_dict(model):
        if hasattr(model, "model_dump"):
            return model.model_dump(exclude_unset=True)
        return model.dict(exclude_unset=True)
