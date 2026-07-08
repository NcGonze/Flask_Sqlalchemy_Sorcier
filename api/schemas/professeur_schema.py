from typing import Optional

from pydantic import BaseModel, Field


class ProfesseurCreateDTO(BaseModel):
    nom: str = Field(..., min_length=1, max_length=50)
    matiere: str = Field(..., min_length=1, max_length=50)
    anciennete: str = Field(..., min_length=1, max_length=50)


class ProfesseurUpdateDTO(BaseModel):
    nom: Optional[str] = Field(default=None, min_length=1, max_length=50)
    matiere: Optional[str] = Field(default=None, min_length=1, max_length=50)
    anciennete: Optional[str] = Field(default=None, min_length=1, max_length=50)
