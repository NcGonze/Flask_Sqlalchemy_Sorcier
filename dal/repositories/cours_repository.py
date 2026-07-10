from dal.database import get_db
from dal.models.cours import Cour
from dal.models.eleve import Eleve


class CoursRepository:

    
    def get_all(self):
        with get_db() as db:
            query = db.query(Cour).order_by(Cour.cours_id.asc()).all()
            return [self._serialize_cours(cours) for cours in query]

    
    def get_by_id(self, cours_id):
        with get_db() as db:
            cours = db.query(Cour).filter(Cour.cours_id == cours_id).first()
            return self._serialize_cours(cours) if cours else None

    
    def create(self, data):
        with get_db() as db:
            cours = Cour(**data)
            db.add(cours)
            db.flush()
            return self._serialize_cours(cours)

    def update(self, cours_id, data):
        with get_db() as db:
            cours = db.query(Cour).filter(Cour.cours_id == cours_id).first()
            if cours is None:
                return None

            for field, value in data.items():
                setattr(cours, field, value)

            db.flush()
            return self._serialize_cours(cours)

    def delete(self, cours_id):
        with get_db() as db:
            cours = db.query(Cour).filter(Cour.cours_id == cours_id).first()
            if cours is None:
                return False

            db.delete(cours)
            return True
    
    def add_eleve(self, cours_id, eleve_id):
        with get_db() as db:
            cour = db.query(Cour).filter(Cour.cours_id == cours_id)
            eleve = db.query(Eleve).filter(Eleve.eleve_id == eleve_id)
            cour.eleves.append(eleve) # type: ignore
            db.flush()
            return self._serialize_cours(cour)
    
    def get_capacite(self,cour_id):
        with get_db() as db:
            cour = db.query(Cour).filter(Cour.cours_id == cour_id)
            cap = cour.capacite_max # type: ignore
            nbre = cour.eleves # type: ignore
            return cap, nbre
        
    @staticmethod
    def _serialize_cours(cours):
        if cours is None:
            return None

        
        return {
            "id": cours.cours_id,
            "intitule": cours.intitule,
            "niveau_requis": cours.niveau_requis,
            "capacite_max": cours.capacite_max,
            "annee": cours.annee,
            "professeur_id": cours.professeur_id,
            "professeur": cours.professeur.nom if cours.professeur else None,
        }
