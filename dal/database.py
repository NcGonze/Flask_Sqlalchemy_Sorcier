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

engine = create_engine(DATABASE_URL, echo=False) # type: ignore

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

        # Maisons (4)
        maisons = [
            Maison(nom="Gryffondor", fondateur="Godric Gryffindor", valeurs="courage"),
            Maison(nom="Serpentard", fondateur="Salazar Slytherin", valeurs="ambition"),
            Maison(nom="Poufsouffle", fondateur="Helga Hufflepuff", valeurs="loyauté"),
            Maison(nom="Serdaigle", fondateur="Rowena Ravenclaw", valeurs="sagesse"),
        ]
        db.add_all(maisons)

        # Utilisateurs: admin + tous les élèves et professeurs
        utilisateurs = [
            Utilisateur(email="admin@hogwarts.local", mot_de_passe="adminpass", role="admin"),
            Utilisateur(email="harry.potter@hogwarts.local", mot_de_passe="pass123", role="eleve"),
            Utilisateur(email="hermione.granger@hogwarts.local", mot_de_passe="pass123", role="eleve"),
            Utilisateur(email="ron.weasley@hogwarts.local", mot_de_passe="pass123", role="eleve"),
            Utilisateur(email="luna.lovegood@hogwarts.local", mot_de_passe="pass123", role="eleve"),
            Utilisateur(email="neville.longbottom@hogwarts.local", mot_de_passe="pass123", role="eleve"),
            Utilisateur(email="ginny.weasley@hogwarts.local", mot_de_passe="pass123", role="eleve"),
            Utilisateur(email="draco.malfoy@hogwarts.local", mot_de_passe="pass123", role="eleve"),
            Utilisateur(email="cedric.diggory@hogwarts.local", mot_de_passe="pass123", role="eleve"),
            Utilisateur(email="cho.chang@hogwarts.local", mot_de_passe="pass123", role="eleve"),
            Utilisateur(email="dean.thomas@hogwarts.local", mot_de_passe="pass123", role="eleve"),
            Utilisateur(email="seamus.finnigan@hogwarts.local", mot_de_passe="pass123", role="eleve"),
            Utilisateur(email="parvati.patil@hogwarts.local", mot_de_passe="pass123", role="eleve"),
            Utilisateur(email="padma.patil@hogwarts.local", mot_de_passe="pass123", role="eleve"),
            Utilisateur(email="sirius.black@hogwarts.local", mot_de_passe="pass123", role="eleve"),
            Utilisateur(email="james.potter@hogwarts.local", mot_de_passe="pass123", role="eleve"),
            Utilisateur(email="lily.evans@hogwarts.local", mot_de_passe="pass123", role="eleve"),
            Utilisateur(email="molly.weasley@hogwarts.local", mot_de_passe="pass123", role="eleve"),
            Utilisateur(email="arthur.weasley@hogwarts.local", mot_de_passe="pass123", role="eleve"),
            Utilisateur(email="fred.weasley@hogwarts.local", mot_de_passe="pass123", role="eleve"),
            Utilisateur(email="george.weasley@hogwarts.local", mot_de_passe="pass123", role="eleve"),
            Utilisateur(email="nymphadora.tonks@hogwarts.local", mot_de_passe="pass123", role="eleve"),
            Utilisateur(email="bellatrix.lestrange@hogwarts.local", mot_de_passe="pass123", role="eleve"),
            Utilisateur(email="lucius.malfoy@hogwarts.local", mot_de_passe="pass123", role="eleve"),
            Utilisateur(email="nicolas.flamel@hogwarts.local", mot_de_passe="pass123", role="eleve"),
            Utilisateur(email="rubeus.hagrid@hogwarts.local", mot_de_passe="pass123", role="eleve"),
            Utilisateur(email="ginevra.weasley@hogwarts.local", mot_de_passe="pass123", role="eleve"),
            Utilisateur(email="oliver.wood@hogwarts.local", mot_de_passe="pass123", role="eleve"),
            Utilisateur(email="susan.bones@hogwarts.local", mot_de_passe="pass123", role="eleve"),
            Utilisateur(email="pansy.parkinson@hogwarts.local", mot_de_passe="pass123", role="eleve"),
            Utilisateur(email="blaise.zabini@hogwarts.local", mot_de_passe="pass123", role="eleve"),
            Utilisateur(email="minerva.mcgonagall@hogwarts.local", mot_de_passe="pass123", role="professeur"),
            Utilisateur(email="severus.snape@hogwarts.local", mot_de_passe="pass123", role="professeur"),
            Utilisateur(email="remus.lupin@hogwarts.local", mot_de_passe="pass123", role="professeur"),
            Utilisateur(email="sybill.trelawney@hogwarts.local", mot_de_passe="pass123", role="professeur"),
            Utilisateur(email="filius.flitwick@hogwarts.local", mot_de_passe="pass123", role="professeur"),
        ]
        db.add_all(utilisateurs)
        db.flush()

        # Professeurs (avec utilisateur_id)
        profs = [
            Professeur(nom="Minerva McGonagall", matiere="Transfiguration", anciennete="20 ans", utilisateur_id=utilisateurs[31].utilisateur_id),
            Professeur(nom="Severus Snape", matiere="Potions", anciennete="15 ans", utilisateur_id=utilisateurs[32].utilisateur_id),
            Professeur(nom="Remus Lupin", matiere="Defense Against the Dark Arts", anciennete="10 ans", utilisateur_id=utilisateurs[33].utilisateur_id),
            Professeur(nom="Sybill Trelawney", matiere="Divination", anciennete="8 ans", utilisateur_id=utilisateurs[34].utilisateur_id),
            Professeur(nom="Filius Flitwick", matiere="Charms", anciennete="18 ans", utilisateur_id=utilisateurs[35].utilisateur_id),
        ]
        db.add_all(profs)
        db.flush()

        # Cours (attach to professeurs)
        cours = [
            Cour(intitule="Métamorphose Avancée", niveau_requis="Intermédiaire", capacite_max=20, professeur_id=profs[0].professeur_id),
            Cour(intitule="Potions Élémentaires", niveau_requis="Débutant", capacite_max=15, professeur_id=profs[1].professeur_id),
            Cour(intitule="Défense contre les forces du Mal", niveau_requis="Intermédiaire", capacite_max=18, professeur_id=profs[2].professeur_id),
            Cour(intitule="Divination Introduction", niveau_requis="Débutant", capacite_max=16, professeur_id=profs[3].professeur_id),
            Cour(intitule="Sortilèges et Charms", niveau_requis="Intermédiaire", capacite_max=22, professeur_id=profs[4].professeur_id),
            Cour(intitule="Histoire de la Magie", niveau_requis="Débutant", capacite_max=20, professeur_id=profs[0].professeur_id),
        ]
        db.add_all(cours)

        # Élèves: 30 répartis sur 7 années et 4 maisons, avec utilisateur_id
        eleves = [
            Eleve(nom="Harry Potter", annee_etude=5, familier="Hedwige", statut="actif", maison_id=maisons[0].maison_id, utilisateur_id=utilisateurs[1].utilisateur_id),
            Eleve(nom="Hermione Granger", annee_etude=5, familier="Crochu", statut="actif", maison_id=maisons[3].maison_id, utilisateur_id=utilisateurs[2].utilisateur_id),
            Eleve(nom="Ron Weasley", annee_etude=5, familier="Scabbers", statut="actif", maison_id=maisons[0].maison_id, utilisateur_id=utilisateurs[3].utilisateur_id),
            Eleve(nom="Luna Lovegood", annee_etude=3, familier="Furet", statut="actif", maison_id=maisons[3].maison_id, utilisateur_id=utilisateurs[4].utilisateur_id),
            Eleve(nom="Neville Longbottom", annee_etude=4, familier="Rat", statut="actif", maison_id=maisons[0].maison_id, utilisateur_id=utilisateurs[5].utilisateur_id),
            Eleve(nom="Ginny Weasley", annee_etude=4, familier="Salamandre", statut="actif", maison_id=maisons[0].maison_id, utilisateur_id=utilisateurs[6].utilisateur_id),
            Eleve(nom="Draco Malfoy", annee_etude=6, familier="Serpent", statut="actif", maison_id=maisons[1].maison_id, utilisateur_id=utilisateurs[7].utilisateur_id),
            Eleve(nom="Cedric Diggory", annee_etude=5, familier="Chouette", statut="actif", maison_id=maisons[2].maison_id, utilisateur_id=utilisateurs[8].utilisateur_id),
            Eleve(nom="Cho Chang", annee_etude=6, familier="Oiseau", statut="actif", maison_id=maisons[3].maison_id, utilisateur_id=utilisateurs[9].utilisateur_id),
            Eleve(nom="Dean Thomas", annee_etude=3, familier="Chien", statut="actif", maison_id=maisons[0].maison_id, utilisateur_id=utilisateurs[10].utilisateur_id),
            Eleve(nom="Seamus Finnigan", annee_etude=3, familier="Chat", statut="actif", maison_id=maisons[0].maison_id, utilisateur_id=utilisateurs[11].utilisateur_id),
            Eleve(nom="Parvati Patil", annee_etude=4, familier="Faucon", statut="actif", maison_id=maisons[0].maison_id, utilisateur_id=utilisateurs[12].utilisateur_id),
            Eleve(nom="Padma Patil", annee_etude=4, familier="Chouette", statut="actif", maison_id=maisons[3].maison_id, utilisateur_id=utilisateurs[13].utilisateur_id),
            Eleve(nom="Sirius Black", annee_etude=7, familier="Chien", statut="actif", maison_id=maisons[0].maison_id, utilisateur_id=utilisateurs[14].utilisateur_id),
            Eleve(nom="James Potter", annee_etude=7, familier="Cerf", statut="actif", maison_id=maisons[0].maison_id, utilisateur_id=utilisateurs[15].utilisateur_id),
            Eleve(nom="Lily Evans", annee_etude=7, familier="Chat", statut="actif", maison_id=maisons[3].maison_id, utilisateur_id=utilisateurs[16].utilisateur_id),
            Eleve(nom="Molly Weasley", annee_etude=7, familier="Aigle", statut="actif", maison_id=maisons[0].maison_id, utilisateur_id=utilisateurs[17].utilisateur_id),
            Eleve(nom="Arthur Weasley", annee_etude=7, familier="Hibou", statut="actif", maison_id=maisons[0].maison_id, utilisateur_id=utilisateurs[18].utilisateur_id),
            Eleve(nom="Fred Weasley", annee_etude=6, familier="Rat", statut="actif", maison_id=maisons[0].maison_id, utilisateur_id=utilisateurs[19].utilisateur_id),
            Eleve(nom="George Weasley", annee_etude=6, familier="Rat", statut="actif", maison_id=maisons[0].maison_id, utilisateur_id=utilisateurs[20].utilisateur_id),
            Eleve(nom="Nymphadora Tonks", annee_etude=6, familier="Chouette", statut="actif", maison_id=maisons[1].maison_id, utilisateur_id=utilisateurs[21].utilisateur_id),
            Eleve(nom="Bellatrix Lestrange", annee_etude=7, familier="Serpent", statut="actif", maison_id=maisons[1].maison_id, utilisateur_id=utilisateurs[22].utilisateur_id),
            Eleve(nom="Lucius Malfoy", annee_etude=7, familier="Serpent", statut="actif", maison_id=maisons[1].maison_id, utilisateur_id=utilisateurs[23].utilisateur_id),
            Eleve(nom="Nicolas Flamel", annee_etude=7, familier="Aigle", statut="actif", maison_id=maisons[3].maison_id, utilisateur_id=utilisateurs[24].utilisateur_id),
            Eleve(nom="Rubeus Hagrid", annee_etude=1, familier="Cochon", statut="actif", maison_id=maisons[2].maison_id, utilisateur_id=utilisateurs[25].utilisateur_id),
            Eleve(nom="Ginevra Weasley", annee_etude=5, familier="Chat", statut="actif", maison_id=maisons[0].maison_id, utilisateur_id=utilisateurs[26].utilisateur_id),
            Eleve(nom="Oliver Wood", annee_etude=3, familier="Chien", statut="actif", maison_id=maisons[0].maison_id, utilisateur_id=utilisateurs[27].utilisateur_id),
            Eleve(nom="Susan Bones", annee_etude=2, familier="Loutre", statut="actif", maison_id=maisons[2].maison_id, utilisateur_id=utilisateurs[28].utilisateur_id),
            Eleve(nom="Pansy Parkinson", annee_etude=5, familier="Chat", statut="actif", maison_id=maisons[1].maison_id, utilisateur_id=utilisateurs[29].utilisateur_id),
            Eleve(nom="Blaise Zabini", annee_etude=6, familier="Serpent", statut="actif", maison_id=maisons[1].maison_id, utilisateur_id=utilisateurs[30].utilisateur_id),
            Eleve(nom="Fleur Delacour", annee_etude=6, familier="Faisan", statut="actif", maison_id=maisons[2].maison_id, utilisateur_id=utilisateurs[31].utilisateur_id),
        ]
        db.add_all(eleves)

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