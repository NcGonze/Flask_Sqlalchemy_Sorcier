from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String, Integer, DateTime
from .base import Base
from datetime import datetime
# from .professeur import Professeur

class Cour(Base):
    __tablename__ = "cours"

    cours_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    intitule: Mapped[str] = mapped_column(String(50), nullable=False)
    niveau_requis: Mapped[str] = mapped_column(String(50))
    capacite_max: Mapped[int] = mapped_column(Integer)
    annee: Mapped[int] = mapped_column(Integer, default=datetime.now().year)
    professeur_id: Mapped[int] = mapped_column(Integer, ForeignKey("professeurs.professeur_id"), nullable=False)

    professeur: Mapped["Professeur"] = relationship( back_populates="cours") # type: ignore
    