from .base import Base
from sqlalchemy import Column, Integer, Text, Boolean, DateTime, String
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .eleve import Eleve

class Maison(Base):

    __tablename__ = "maisons"

    maison_id: Mapped[int] = mapped_column(Integer,primary_key = True, autoincrement=True)
    nom: Mapped[str] = mapped_column(String(50), nullable=False)
    fondateur : Mapped[str] = mapped_column(String(50))
    valeurs: Mapped[str] = mapped_column(String(50))

    eleves: Mapped[list["Eleve"]] = relationship(back_populates="maison")