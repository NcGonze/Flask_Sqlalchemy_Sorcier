from pydantic import BaseModel, Field


class MaisonCreateDTO(BaseModel):
    nom: str = Field(..., min_length=1, max_length=50)
    fondateur: str = Field(..., min_length=1, max_length=50)
    valeurs: str = Field(..., min_length=1, max_length=50)
