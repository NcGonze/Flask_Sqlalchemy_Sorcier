import os
from dotenv import load_dotenv
from api.auth_helpers import InvalidUserHeaderError, MissingUserHeaderError
from api.routes.auth_route import auth_bp
from api.routes.task_routes import task_bp
from api.routes.maison_routes import maisons_bp

from api.routes.cours_routes import cours_bp
from api.routes.eleve_routes import eleves_bp
from api.routes.professeur_routes import professeurs_bp
from flask import Flask, jsonify
from dal.database import try_coonection, init_db, seed_data

load_dotenv()

app = Flask(__name__)
app.json.sort_keys = False # type: ignore
app.register_blueprint(auth_bp)
app.register_blueprint(task_bp)
app.register_blueprint(maisons_bp)

app.register_blueprint(cours_bp)
app.register_blueprint(eleves_bp)
app.register_blueprint(professeurs_bp)


@app.errorhandler(MissingUserHeaderError)
def missing_user_header(error):
    return jsonify({"error": str(error)}), 401


@app.errorhandler(InvalidUserHeaderError)
def invalid_user_header(error):
    return jsonify({"error": str(error)}), 400

def startup():
    if try_coonection():
        init_db(delete = True)
        seed_data()
        print("db lancé")

startup()

@app.route('/')
def home():
    return jsonify({"test" : "yo"})

if __name__ == '__main__':

    app.run(debug=True, port=5000)
