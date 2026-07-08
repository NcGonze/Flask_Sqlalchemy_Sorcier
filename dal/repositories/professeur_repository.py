import re
import unicodedata

from dal.database import get_db
from dal.models.professeur import Professeur
from dal.models.utilisateur import Utilisateur


class ProfesseurRepository:

    def get_all(self):
        with get_db() as db:
            query = db.query(Professeur).order_by(Professeur.professeur_id.asc()).all()
            return [self._serialize_professeur(professeur) for professeur in query]

    def get_by_id(self, professeur_id):
        with get_db() as db:
            professeur = db.query(Professeur).filter(Professeur.professeur_id == professeur_id).first()
            return self._serialize_professeur(professeur) if professeur else None

    def create(self, data):
        with get_db() as db:
            utilisateur = Utilisateur(
                email=self._build_email(db, data["nom"]),
                mot_de_passe="pass123",
                role="professeur",
            )
            db.add(utilisateur)
            db.flush()

            professeur = Professeur(**data, utilisateur_id=utilisateur.utilisateur_id)
            db.add(professeur)
            db.flush()
            return self._serialize_professeur(professeur)

    def update(self, professeur_id, data):
        with get_db() as db:
            professeur = db.query(Professeur).filter(Professeur.professeur_id == professeur_id).first()
            if professeur is None:
                return None

            for field, value in data.items():
                setattr(professeur, field, value)

            db.flush()
            return self._serialize_professeur(professeur)

    def delete(self, professeur_id):
        with get_db() as db:
            professeur = db.query(Professeur).filter(Professeur.professeur_id == professeur_id).first()
            if professeur is None:
                return False

            utilisateur = professeur.utilisateur_p
            db.delete(professeur)
            if utilisateur is not None:
                db.delete(utilisateur)
            return True

    @staticmethod
    def _serialize_professeur(professeur):
        if professeur is None:
            return None

        return {
            "id": professeur.professeur_id,
            "nom": professeur.nom,
            "matiere": professeur.matiere,
            "anciennete": professeur.anciennete,
            "utilisateur_id": professeur.utilisateur_id,
            "email": professeur.utilisateur_p.email if professeur.utilisateur_p else None,
            "cours": [cours.intitule for cours in professeur.cours],
        }

    @staticmethod
    def _slugify_name(nom):
        normalized = unicodedata.normalize("NFKD", nom)
        ascii_name = normalized.encode("ascii", "ignore").decode("ascii")
        slug = re.sub(r"[^a-z0-9]+", ".", ascii_name.lower()).strip(".")
        return slug or "utilisateur"

    def _build_email(self, db, nom):
        base = self._slugify_name(nom)
        domain = "@hogwarts.local"
        local_max_length = 50 - len(domain)
        base = base[:local_max_length].strip(".") or "utilisateur"
        email = f"{base}{domain}"
        index = 2

        while db.query(Utilisateur).filter(Utilisateur.email == email).first() is not None:
            suffix = f".{index}"
            local = base[:local_max_length - len(suffix)].strip(".")
            email = f"{local}{suffix}{domain}"
            index += 1

        return email
