from dal.database import get_db
from dal.models.eleve import Eleve
from dal.models.professeur import Professeur
from dal.models.utilisateur import Utilisateur


class AuthRepository():

    def match(self, email, mot_de_passe):
        with get_db() as db:
            utilisateur = db.query(Utilisateur).filter(
                Utilisateur.email == email,
                Utilisateur.mot_de_passe == mot_de_passe,
            ).first()

            if utilisateur is None:
                return None

            identifiant_lie = self._get_identifiant_lie(db, utilisateur)

            return {
                "utilisateur_id": utilisateur.utilisateur_id,
                "email": utilisateur.email,
                "role": utilisateur.role,
                "identifiant_lie": identifiant_lie,
            }

    @staticmethod
    def _get_identifiant_lie(db, utilisateur):
        if utilisateur.role == "eleve":
            eleve = db.query(Eleve).filter(Eleve.utilisateur_id == utilisateur.utilisateur_id).first()
            return eleve.eleve_id if eleve else None

        if utilisateur.role == "professeur":
            professeur = db.query(Professeur).filter(
                Professeur.utilisateur_id == utilisateur.utilisateur_id
            ).first()
            return professeur.professeur_id if professeur else None

        return None
