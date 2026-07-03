# Flask Task API

Petite API Flask pour gérer des tâches.

## Installation

1. Crée un environnement virtuel Python :
   ```bash
   python -m venv .venv
   ```
2. Active-le :
   - Windows PowerShell : `.\.venv\Scripts\Activate.ps1`
   - Windows CMD : `.\.venv\Scripts\activate.bat`
3. Installe les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

## Lancement

Depuis le dossier racine du projet :

```bash
python api/app.py
```

L’application tourne par défaut sur `http://127.0.0.1:5000`.

## Endpoints

- `GET /api/tasks`
- `GET /api/tasks?done=true` ou `done=false`
- `GET /api/tasks/<id>`
- `POST /api/tasks`
- `PUT /api/tasks/<id>`
- `DELETE /api/tasks/<id>`

## Exemple de corps JSON

Pour créer ou mettre à jour une tâche :

```json
{
  "titre": "Nouvelle task",
  "description": "Description",
  "done": false
}
```

## Notes

- `POST` et `PUT` attendent un `Content-Type: application/json`.
- Les données sont validées avant d’être envoyées en base.
