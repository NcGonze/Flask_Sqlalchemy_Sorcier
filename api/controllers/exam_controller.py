from typing import Any

from api.schemas.cours_schema import CoursCreateDTO, CoursUpdateDTO
from dal.repositories.exam_repository import ExamenRepository


class ExamenController:

    def __init__(self):
        self.repo = ExamenRepository()
    
    def result_exam(self,exam_id,payload):
        pass