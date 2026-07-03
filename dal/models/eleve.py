from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String, Integer
from .database import Base
from .maison import Maison

class Eleve(Base):
    __tablename__ = "eleves"

    eleve_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nom: Mapped[str] = mapped_column(String(50), nullable=False)
    annee_etude: Mapped[int] = mapped_column(Integer)
    familier: Mapped[str] = mapped_column(String(50))
    statut: Mapped[str] = mapped_column(String(50), default="actif")
    maison_id: Mapped[int] = mapped_column(Integer, ForeignKey("maisons.maison_id"), nullable=False)

    maison: Mapped["Maison"] = relationship(back_populates="eleves")
    