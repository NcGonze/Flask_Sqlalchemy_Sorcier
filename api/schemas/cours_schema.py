from typing import Optional

from pydantic import BaseModel, Field


# HIGHLIGHT: nouveau DTO pour la creation d'un cours.
class CoursCreateDTO(BaseModel):
    intitule: str = Field(..., min_length=1, max_length=50)
    niveau_requis: str = Field(..., min_length=1, max_length=50)
    capacite_max: int = Field(..., ge=1)
    annee: Optional[int] = Field(default=None, ge=1)
    professeur_id: int = Field(..., ge=1)


# HIGHLIGHT: nouveau DTO pour la modification partielle d'un cours.
class CoursUpdateDTO(BaseModel):
    intitule: Optional[str] = Field(default=None, min_length=1, max_length=50)
    niveau_requis: Optional[str] = Field(default=None, min_length=1, max_length=50)
    capacite_max: Optional[int] = Field(default=None, ge=1)
    annee: Optional[int] = Field(default=None, ge=1)
    professeur_id: Optional[int] = Field(default=None, ge=1)
