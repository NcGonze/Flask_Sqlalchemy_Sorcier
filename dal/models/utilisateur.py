from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer
from .base import Base


class Utilisateur(Base):
    __tablename__ = "utilisateurs"

    utilisateur_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(String(50), nullable=False)
    mot_de_passe: Mapped[str] = mapped_column(String(50), nullable=False)
    role: Mapped[str] = mapped_column(String(50))

    eleve: Mapped["Eleve"] = relationship(back_populates="utilisateur_e") # type: ignore
    professeur: Mapped["Professeur"] = relationship(back_populates="utilisateur_p") # type: ignore