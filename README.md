# Sorcier API

API Flask pour gérer une école de magie : maisons, élèves, professeurs, cours, authentification et tâches de démonstration.

Le projet utilise Flask pour l'API, SQLAlchemy pour l'accès aux données, Pydantic pour la validation des payloads et `pyodbc` pour la connexion à la base.

## Structure du projet

```text
api/
  app.py                 Point d'entrée Flask
  routes/                Définition des endpoints
  controllers/           Validation applicative et orchestration
  schemas/               DTO Pydantic
dal/
  database.py            Connexion, création des tables et seed
  models/                Modèles SQLAlchemy
  repositories/          Requêtes base de données
```

## Installation

Créer et activer un environnement virtuel :

```bash
python -m venv .venv
```

Windows PowerShell :

```bash
.\.venv\Scripts\Activate.ps1
```

Installer les dépendances :

```bash
pip install -r requirements.txt
```

## Configuration

Créer un fichier `.env` à la racine du projet avec la chaîne de connexion SQLAlchemy :

```env
CONNECTION_STRING=...
```

Exemple de format avec SQL Server et `pyodbc` :

```env
CONNECTION_STRING=mssql+pyodbc://user:password@server/database?driver=ODBC+Driver+17+for+SQL+Server
```

## Lancement

Depuis la racine du projet :

```bash
python api/app.py
```

L'API démarre par défaut sur :

```text
http://127.0.0.1:5000
```

Attention : au démarrage, `api/app.py` appelle `init_db(delete=True)`, ce qui supprime puis recrée les tables avant d'insérer les données de test.

## Endpoints disponibles

### Accueil

```http
GET /
```

### Authentification

```http
POST /login
```

Payload :

```json
{
  "email": "admin@hogwarts.local",
  "mot_de_passe": "adminpass"
}
```

### Maisons

Préfixe : `/api/maison`

```http
GET    /api/maison
GET    /api/maison/<maison_id>
POST   /api/maison
PUT    /api/maison/<maison_id>
DELETE /api/maison/<maison_id>
```

Payload de création :

```json
{
  "nom": "Gryffondor",
  "fondateur": "Godric Gryffindor",
  "valeurs": "courage"
}
```

### Élèves

Préfixe : `/api/eleves`

```http
GET    /api/eleves
GET    /api/eleves/<eleve_id>
POST   /api/eleves
PUT    /api/eleves/<eleve_id>
DELETE /api/eleves/<eleve_id>
```

Payload de création :

```json
{
  "nom": "Harry Potter",
  "annee_etude": 5,
  "familier": "Hedwige",
  "statut": "actif",
  "maison_id": 1
}
```

### Professeurs

Préfixe : `/api/professeurs`

```http
GET    /api/professeurs
GET    /api/professeurs/<professeur_id>
POST   /api/professeurs
PUT    /api/professeurs/<professeur_id>
DELETE /api/professeurs/<professeur_id>
```

Payload de création :

```json
{
  "nom": "Minerva McGonagall",
  "matiere": "Transfiguration",
  "anciennete": "20 ans"
}
```

### Cours

Préfixe : `/api/cours`

```http
GET    /api/cours
GET    /api/cours/<cours_id>
POST   /api/cours
PUT    /api/cours/<cours_id>
DELETE /api/cours/<cours_id>
PUT    /api/cours/sign/<cours_id>
```

Payload de création :

```json
{
  "intitule": "Potions élémentaires",
  "niveau_requis": "Débutant",
  "capacite_max": 15,
  "annee": 2026,
  "professeur_id": 1
}
```

La route `/api/cours/sign/<cours_id>` est prévue pour inscrire un élève à un cours.

### Tâches

Préfixe : `/api/tasks`

```http
GET    /api/tasks
GET    /api/tasks?done=true
GET    /api/tasks?done=false
GET    /api/tasks/<task_id>
POST   /api/tasks
PUT    /api/tasks/<task_id>
DELETE /api/tasks/<task_id>
```

Payload de création :

```json
{
  "titre": "Préparer le cours",
  "description": "Créer les supports",
  "done": false
}
```

## Fonctionnalités en cours

Le dossier contient aussi des fichiers pour les examens :

```text
api/routes/exam_route.py
api/controllers/exam_controller.py
dal/repositories/exam_repository.py
```

Cette partie semble encore en développement : le blueprint `exam_bp` n'est pas enregistré dans `api/app.py` et le repository est vide.

## Données de test

Au démarrage, `seed_data()` insère notamment :

- 4 maisons
- 1 administrateur
- des utilisateurs élèves et professeurs
- plusieurs professeurs
- plusieurs cours
- une liste d'élèves

Identifiants utiles :

```text
admin@hogwarts.local / adminpass
harry.potter@hogwarts.local / pass123
minerva.mcgonagall@hogwarts.local / pass123
```

## Validation

Les données entrantes sont validées avec des DTO Pydantic dans `api/schemas`.

Exemples :

- `CoursCreateDTO` vérifie l'intitulé, le niveau requis, la capacité, l'année et le professeur.
- `EleveCreateDTO` vérifie le nom, l'année d'étude, le familier, le statut et la maison.
- `LoginDTO` vérifie l'email et le mot de passe.

Les règles métier dynamiques, comme la capacité maximale d'un cours, doivent rester dans les contrôleurs ou repositories, car elles dépendent de l'état de la base.
