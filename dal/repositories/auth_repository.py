from dal.database import get_db
from dal.models.utilisateur import Utilisateur


class AuthRepository():

    def match(self, payload):
        with get_db() as db:
            try:
                res = db.query(Utilisateur).filter(Utilisateur.email == payload.email and Utilisateur.mot_de_passe == payload.mot_de_passe)
                return res
            except Exception as e:
                return None
            
