import re
import unicodedata

from dal.database import get_db
from dal.models.eleve import Eleve
from dal.models.maison import Maison
from dal.models.utilisateur import Utilisateur


class EleveRepository:

    def get_all(self):
        with get_db() as db:
            query = db.query(Eleve).order_by(Eleve.eleve_id.asc()).all()
            return [self._serialize_eleve(eleve) for eleve in query]

    def get_by_id(self, eleve_id):
        with get_db() as db:
            eleve = db.query(Eleve).filter(Eleve.eleve_id == eleve_id).first()
            return self._serialize_eleve(eleve) if eleve else None

    def create(self, data):
        with get_db() as db:
            maison = db.query(Maison).filter(Maison.maison_id == data["maison_id"]).first()
            if maison is None:
                raise ValueError("Maison not found")

            utilisateur = Utilisateur(
                email=self._build_email(db, data["nom"]),
                mot_de_passe="pass123",
                role="eleve",
            )
            db.add(utilisateur)
            db.flush()

            eleve = Eleve(**data, utilisateur_id=utilisateur.utilisateur_id)
            db.add(eleve)
            db.flush()
            return self._serialize_eleve(eleve)

    def update(self, eleve_id, data):
        with get_db() as db:
            eleve = db.query(Eleve).filter(Eleve.eleve_id == eleve_id).first()
            if eleve is None:
                return None

            if "maison_id" in data:
                maison = db.query(Maison).filter(Maison.maison_id == data["maison_id"]).first()
                if maison is None:
                    raise ValueError("Maison not found")

            for field, value in data.items():
                setattr(eleve, field, value)

            db.flush()
            return self._serialize_eleve(eleve)

    def delete(self, eleve_id):
        with get_db() as db:
            eleve = db.query(Eleve).filter(Eleve.eleve_id == eleve_id).first()
            if eleve is None:
                return False

            utilisateur = eleve.utilisateur_e
            db.delete(eleve)
            if utilisateur is not None:
                db.delete(utilisateur)
            return True

    @staticmethod
    def _serialize_eleve(eleve):
        if eleve is None:
            return None

        return {
            "id": eleve.eleve_id,
            "nom": eleve.nom,
            "annee_etude": eleve.annee_etude,
            "familier": eleve.familier,
            "statut": eleve.statut,
            "maison_id": eleve.maison_id,
            "maison": eleve.maison.nom if eleve.maison else None,
            "utilisateur_id": eleve.utilisateur_id,
            "email": eleve.utilisateur_e.email if eleve.utilisateur_e else None,
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
