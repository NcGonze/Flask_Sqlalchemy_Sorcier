from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String, Integer
from .base import Base
from .cours import Cour

class Professeur(Base):
    __tablename__ = "professeurs"

    professeur_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nom: Mapped[str] = mapped_column(String(50), nullable=False)
    matiere: Mapped[str] = mapped_column(String(50))
    anciennete : Mapped[str] = mapped_column(String(50))
    utilisateur_id: Mapped[int] = mapped_column(Integer, ForeignKey("utilisateurs.utilisateur_id"),nullable=False)

    cours: Mapped[list["Cour"]] = relationship(back_populates="professeur")
    utilisateur_p : Mapped["Utilisateur"] = relationship(back_populates ="professeur") # type: ignore