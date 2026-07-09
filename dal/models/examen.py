from datetime import datetime, date

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Date, String, Integer
from .base import Base

class Examen(Base):
    __tablename__ = "examens"

    examen_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    titre: Mapped[str] = mapped_column(String(50), nullable=False)
    date: Mapped[datetime] = mapped_column(Date, default=datetime.now())
    seuil_reussite: Mapped[int] = mapped_column(Integer, default=10)
    
    cour_ex: Mapped["Cour"] = relationship(back_populates="examens") # type: ignore
    eleves_res: Mapped[list["Eleve"]] = relationship(back_populates="examens_res", secondary="examens_eleves") # type: ignore