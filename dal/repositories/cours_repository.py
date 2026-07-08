from dal.database import get_db
from dal.models.cours import Cour


class CoursRepository:

    # HIGHLIGHT: liste tous les cours.
    def get_all(self):
        with get_db() as db:
            query = db.query(Cour).order_by(Cour.cours_id.asc()).all()
            return [self._serialize_cours(cours) for cours in query]

    # HIGHLIGHT: recupere un cours par id.
    def get_by_id(self, cours_id):
        with get_db() as db:
            cours = db.query(Cour).filter(Cour.cours_id == cours_id).first()
            return self._serialize_cours(cours) if cours else None

    # HIGHLIGHT: cree un nouveau cours.
    def create(self, data):
        with get_db() as db:
            cours = Cour(**data)
            db.add(cours)
            db.flush()
            return self._serialize_cours(cours)

    # HIGHLIGHT: modifie un cours existant.
    def update(self, cours_id, data):
        with get_db() as db:
            cours = db.query(Cour).filter(Cour.cours_id == cours_id).first()
            if cours is None:
                return None

            for field, value in data.items():
                setattr(cours, field, value)

            db.flush()
            return self._serialize_cours(cours)

    # HIGHLIGHT: supprime un cours existant.
    def delete(self, cours_id):
        with get_db() as db:
            cours = db.query(Cour).filter(Cour.cours_id == cours_id).first()
            if cours is None:
                return False

            db.delete(cours)
            return True

    @staticmethod
    def _serialize_cours(cours):
        if cours is None:
            return None

        # HIGHLIGHT: format JSON renvoye par l'API pour un cours.
        return {
            "id": cours.cours_id,
            "intitule": cours.intitule,
            "niveau_requis": cours.niveau_requis,
            "capacite_max": cours.capacite_max,
            "annee": cours.annee,
            "professeur_id": cours.professeur_id,
            "professeur": cours.professeur.nom if cours.professeur else None,
        }
