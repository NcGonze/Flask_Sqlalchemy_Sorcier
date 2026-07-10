from dal.database import get_db
from dal.models.maison import Maison


class MaisonRepository:

    # HIGHLIGHT: get_data remplace par un get_all plus coherent avec les autres repositories.
    def get_all(self):
        with get_db() as db:
            query = db.query(Maison).order_by(Maison.maison_id.asc()).all()
            return [self._serialize_maison(e) for e in query]

    # HIGHLIGHT: recuperation d'une seule maison.
    def get_by_id(self, maison_id):
        with get_db() as db:
            maison = db.query(Maison).filter(Maison.maison_id == maison_id).first()
            return self._serialize_maison(maison) if maison else None

    def create(self, data):
        with get_db() as db:
            maison = Maison(**data)
            db.add(maison)
            db.flush()
            return self._serialize_maison(maison)

    # HIGHLIGHT: modification champ par champ avec les donnees validees par le DTO.
    def update(self, maison_id, data):
        with get_db() as db:
            maison = db.query(Maison).filter(Maison.maison_id == maison_id).first()
            if maison is None:
                return None

            for field, value in data.items():
                setattr(maison, field, value)

            db.flush()
            return self._serialize_maison(maison)

    # HIGHLIGHT: suppression avec retour booleen pour gerer le 404 dans la route.
    def delete(self, maison_id):
        with get_db() as db:
            maison = db.query(Maison).filter(Maison.maison_id == maison_id).first()
            if maison is None:
                return False

            db.delete(maison)
            return True

    @staticmethod
    def _serialize_maison(maison):
        if maison is None:
            return None

        return {
            "id": maison.maison_id,
            "nom": maison.nom,
            "fondateur": maison.fondateur,
            "valeurs": maison.valeurs,
            "eleves": [e.nom for e in maison.eleves],
        }
