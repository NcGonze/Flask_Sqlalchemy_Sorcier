import os
from dotenv import load_dotenv
from api.routes.task_routes import task_bp
from flask import Flask, jsonify
from dal.database import try_coonection, init_db, seed_data

load_dotenv()

app = Flask(__name__)
app.json.sort_keys = False
app.register_blueprint(task_bp)

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