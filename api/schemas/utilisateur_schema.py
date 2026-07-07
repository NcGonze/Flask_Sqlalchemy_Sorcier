from typing import Optional
from pydantic import BaseModel, root_validator, EmailStr, Field, model_validator


class UtilisateurCreateDTO(BaseModel):
    email: EmailStr
    mot_de_passe: str = Field(..., min_length=6)
    role: str = Field(default="eleve")
    eleve_id: Optional[int] = None
    professeur_id: Optional[int] = None




class UtilisateurUpdateDTO(BaseModel):
    email: Optional[EmailStr] = None
    mot_de_passe: Optional[str] = Field(default=None, min_length=6)
    role: Optional[str] = None
    eleve_id: Optional[int] = None
    professeur_id: Optional[int] = None

