from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String, Integer, Email
from .database import Base
from dal.models.eleve import Eleve
from dal.models.professeur import Professeur


class Utilisateur(Base):
    __tablename__ = "utilisateurs"

    utilisateur_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(Email, nullable=False)
    mot_de_passe: Mapped[str] = mapped_column(String(20), nullable=False)
    role: Mapped[str] = mapped_column(String(20), default="eleve")

    eleve_id: Mapped[int] = mapped_column(Integer, ForeignKey("eleves.eleve_id"), nullable=True)
    professeur_id: Mapped[int] = mapped_column(Integer, ForeignKey("professeurs.professeur_id"), nullable=True)

    eleve: Mapped["Eleve"] = relationship("Eleve", uselist=False)
    professeur: Mapped["Professeur"] = relationship("Professeur", uselist=False)