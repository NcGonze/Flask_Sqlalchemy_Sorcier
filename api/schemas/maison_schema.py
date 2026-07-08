from typing import Optional

from pydantic import BaseModel, Field


class MaisonCreateDTO(BaseModel):
    nom: str = Field(..., min_length=1, max_length=50)
    fondateur: str = Field(..., min_length=1, max_length=50)
    valeurs: str = Field(..., min_length=1, max_length=50)


# HIGHLIGHT: DTO ajoute pour valider les donnees lors d'une modification de maison.
class MaisonUpdateDTO(BaseModel):
    nom: Optional[str] = Field(default=None, min_length=1, max_length=50)
    fondateur: Optional[str] = Field(default=None, min_length=1, max_length=50)
    valeurs: Optional[str] = Field(default=None, min_length=1, max_length=50)
