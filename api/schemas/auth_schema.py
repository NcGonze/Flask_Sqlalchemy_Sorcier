from pydantic import BaseModel, Field


class LoginDTO(BaseModel):
    email: str = Field(..., min_length=1, max_length=50)
    mot_de_passe: str = Field(..., min_length=1, max_length=50)
