from api.models.maison import Maison
from .database import get_db

class MaisonRepository:

    def get_data(self):
        with get_db as db:
            query = db.query(Maison)
            return [self._serialize_maison(e) for e in query]
    @staticmethod
    def _serialize_maison(maison):
        if maison is None:
            return None

        return {
            "id": maison.maison_id,
            "nom": maison.nom,
            "fondateur": maison.fondateur,
            "valeur": maison.valeurs,
            "elèves": maison.eleves
        }