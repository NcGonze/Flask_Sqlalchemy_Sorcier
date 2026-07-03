from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import os
from contextlib import contextmanager
from dotenv import load_dotenv
from dal.models.base import Base
from dal.models.maison import Maison
from dal.models.professeur import Professeur
from dal.models.cours import Cour
from dal.models.eleve import Eleve
from dal.models.utilisateur import Utilisateur
from datetime import datetime

load_dotenv()

DATABASE_URL = os.getenv("CONNECTION_STRING")

print(os.getenv("CONNECTION_STRING"))

engine = create_engine(DATABASE_URL, echo=False)

session_local = sessionmaker(autoflush=False, autocommit=False, bind=engine)

def init_db(delete = False):
    if delete:
        Base.metadata.drop_all(bind = engine)
        print("tables vides")
    Base.metadata.create_all(bind = engine)
    print("tables créées youhou")

def try_coonection():
    try:
        with engine.connect() as conn:
            conn.execute(text('SELECT 1'))
            print("connexion établie")
            return True
    except Exception as e:
        print(f"connection erreur : {e}")
        return False

def seed_data():
    with get_db() as db:
        # Seed only if no maisons exist (assume DB empty)
        if db.query(Maison).count() == 0:
            # Maisons
            maisons = [
                Maison(nom="Gryffondor", fondateur="Godric Gryffindor", valeurs="courage"),
                Maison(nom="Serpentard", fondateur="Salazar Slytherin", valeurs="ambition"),
                Maison(nom="Poufsouffle", fondateur="Helga Hufflepuff", valeurs="loyauté"),
                Maison(nom="Serdaigle", fondateur="Rowena Ravenclaw", valeurs="sagesse"),
            ]
            db.add_all(maisons)

            # Professeurs
            profs = [
                Professeur(nom="Minerva McGonagall", matiere="Transfiguration", anciennete="20 ans"),
                Professeur(nom="Severus Snape", matiere="Potions", anciennete="15 ans"),
            ]
            db.add_all(profs)

            db.flush()  # populate IDs for FK usage

            # Cours
            cours = [
                Cour(intitule="Métamorphose Avancée", niveau_requis="Intermédiaire", capacite_max=20, professeur_id=profs[0].professeur_id),
                Cour(intitule="Potions Élémentaires", niveau_requis="Débutant", capacite_max=15, professeur_id=profs[1].professeur_id),
            ]
            db.add_all(cours)

            db.flush()

            # Élèves
            eleves = [
                Eleve(nom="Harry Potter", annee_etude=5, familier="Hedwige", statut="actif", maison_id=maisons[0].maison_id),
                Eleve(nom="Hermione Granger", annee_etude=5, familier="Crochu", statut="actif", maison_id=maisons[3].maison_id),
            ]
            db.add_all(eleves)

            db.flush()

            # Utilisateurs
            utilisateurs = [
                Utilisateur(email="admin@hogwarts.local", mot_de_passe="adminpass", role="admin"),
                Utilisateur(email="harry@hogwarts.local", mot_de_passe="harrypass", role="eleve", eleve_id=eleves[0].eleve_id),
                Utilisateur(email="hermione@hogwarts.local", mot_de_passe="hermpass", role="eleve", eleve_id=eleves[1].eleve_id),
                Utilisateur(email="mcgonagall@hogwarts.local", mot_de_passe="mcgpass", role="professeur", professeur_id=profs[0].professeur_id),
            ]
            db.add_all(utilisateurs)

            print("seed data ajoutée")

@contextmanager
def get_db():
    db = session_local()
    try:
        yield db
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()