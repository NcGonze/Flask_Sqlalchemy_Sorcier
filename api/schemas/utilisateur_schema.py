from typing import Optional
from pydantic import BaseModel, root_validator, EmailStr, Field


class UtilisateurCreateDTO(BaseModel):
    email: EmailStr
    mot_de_passe: str = Field(..., min_length=6)
    role: str = Field(default="eleve")
    eleve_id: Optional[int] = None
    professeur_id: Optional[int] = None

    @root_validator
    def check_role_ids(cls, values):
        role = values.get("role")
        eid = values.get("eleve_id")
        pid = values.get("professeur_id")
        if role == "eleve":
            if eid is None or pid is not None:
                raise ValueError("role=eleve requires eleve_id and professeur_id must be null")
        elif role == "professeur":
            if pid is None or eid is not None:
                raise ValueError("role=professeur requires professeur_id and eleve_id must be null")
        elif role == "admin":
            if eid is not None or pid is not None:
                raise ValueError("role=admin must not have eleve_id or professeur_id")
        else:
            raise ValueError("role invalide, attendu: eleve|professeur|admin")
        return values


class UtilisateurUpdateDTO(BaseModel):
    email: Optional[EmailStr] = None
    mot_de_passe: Optional[str] = Field(default=None, min_length=6)
    role: Optional[str] = None
    eleve_id: Optional[int] = None
    professeur_id: Optional[int] = None

    @root_validator
    def check_role_ids_on_update(cls, values):
        # Only validate if role provided or ids provided
        role = values.get("role")
        eid = values.get("eleve_id")
        pid = values.get("professeur_id")
        if role is None and eid is None and pid is None:
            return values
        if role == "eleve":
            if eid is None or pid is not None:
                raise ValueError("role=eleve requires eleve_id and professeur_id must be null")
        elif role == "professeur":
            if pid is None or eid is not None:
                raise ValueError("role=professeur requires professeur_id and eleve_id must be null")
        elif role == "admin":
            if eid is not None or pid is not None:
                raise ValueError("role=admin must not have eleve_id or professeur_id")
        return values
