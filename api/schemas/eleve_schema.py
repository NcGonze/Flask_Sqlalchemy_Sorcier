from typing import Optional

from pydantic import BaseModel, Field


class EleveCreateDTO(BaseModel):
    nom: str = Field(..., min_length=1, max_length=50)
    annee_etude: int = Field(..., ge=1)
    familier: str = Field(..., min_length=1, max_length=50)
    statut: str = Field(default="actif", min_length=1, max_length=50)
    maison_id: int = Field(..., ge=1)


class EleveUpdateDTO(BaseModel):
    nom: Optional[str] = Field(default=None, min_length=1, max_length=50)
    annee_etude: Optional[int] = Field(default=None, ge=1)
    familier: Optional[str] = Field(default=None, min_length=1, max_length=50)
    statut: Optional[str] = Field(default=None, min_length=1, max_length=50)
    maison_id: Optional[int] = Field(default=None, ge=1)
