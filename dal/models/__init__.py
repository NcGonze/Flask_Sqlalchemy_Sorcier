from sqlalchemy import Column, Date, ForeignKey, Integer, String, Table

from dal.models.base import Base


cours_eleves = Table(
    "cours_eleves",
    Base.metadata,
    Column("cours_id", Integer, ForeignKey("cours.cour_id"),primary_key=True),
    Column("eleve_id", Integer, ForeignKey("eleves.eleve_id"), primary_key=True),
    Column("date_nscription",Date),
    Column("statut", String(50))
)

examens_eleves = Table(
    "examens_eleves",
    Base.metadata,
    Column("examen_id", Integer, ForeignKey("examens.cour_id"),primary_key=True),
    Column("eleve_id", Integer, ForeignKey("eleves.eleve_id"), primary_key=True),
    Column("Note", Integer)
)