from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String, Integer
from .base import Base

class Eleve(Base):
    __tablename__ = "eleves"

    eleve_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nom: Mapped[str] = mapped_column(String(50), nullable=False)
    annee_etude: Mapped[int] = mapped_column(Integer)
    familier: Mapped[str] = mapped_column(String(50))
    statut: Mapped[str] = mapped_column(String(50), default="actif")
    maison_id: Mapped[int] = mapped_column(Integer, ForeignKey("maisons.maison_id"), nullable=False)
    utilisateur_id: Mapped[int] = mapped_column(Integer, ForeignKey("utilisateurs.utilisateur_id"),nullable=False)

    maison: Mapped["Maison"] = relationship(back_populates="eleves") # type: ignore
    utilisateur_e: Mapped['Utilisateur'] = relationship(back_populates = "eleve") # type: ignore
    cours: Mapped['Cour'] = relationship(back_populates="cours", secondary="cours_eleves") # type: ignore
    examens_res: Mapped[list["Examen"]] = relationship(back_populates="eleves_res", secondary="examens_eleves") # type: ignore
    