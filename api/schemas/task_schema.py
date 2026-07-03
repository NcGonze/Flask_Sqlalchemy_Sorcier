from typing import Optional
from pydantic import BaseModel, Field


class TaskFilterDTO(BaseModel):
    done: Optional[bool] = Field(
        default=None,
        description="filtrer par statut (true = fait et false = pas fait)",
    )


class TaskCreateDTO(BaseModel):
    titre: str = Field(..., min_length=1, max_length=200)
    description: Optional[str] = None
    done: bool = False


class TaskUpdateDTO(BaseModel):
    titre: Optional[str] = Field(default=None, min_length=1, max_length=200)
    description: Optional[str] = None
    done: Optional[bool] = None