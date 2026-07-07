from dal.database import get_db
from dal.models.maison import Maison


class MaisonRepository:

    def get_data(self):
        with get_db() as db:
            query = db.query(Maison)
            return [self._serialize_maison(e) for e in query]

    def create(self, data):
        with get_db() as db:
            maison = Maison(**data)
            db.add(maison)
            db.flush()
            return self._serialize_maison(maison)

    @staticmethod
    def _serialize_maison(maison):
        if maison is None:
            return None

        return {
            "id": maison.maison_id,
            "nom": maison.nom,
            "fondateur": maison.fondateur,
            "valeur": maison.valeurs,
            "eleves": [e.nom for e in maison.eleves],
        }
