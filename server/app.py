#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate
from models import db, Pet

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False  # nice formatting for JSON

migrate = Migrate(app, db)
db.init_app(app)

# -------------------------
# ROUTES
# -------------------------

# 1️⃣ Index route
@app.route('/')
def index():
    body = {'message': 'Welcome to the pet directory!'}
    return make_response(body, 200)

# 2️⃣ Get pet by ID
@app.route('/pets/<int:id>')
def pet_by_id(id):
    pet = Pet.query.filter(Pet.id == id).first()

    if pet:
        body = {'id': pet.id,
                'name': pet.name,
                'species': pet.species}
        status = 200
    else:
        body = {'message': f'Pet {id} not found.'}
        status = 404

    return make_response(body, status)

# 3️⃣ Get pets by species
@app.route('/species/<string:species>')
def pet_by_species(species):
    pets = []
    for pet in Pet.query.filter_by(species=species).all():
        pet_dict = {'id': pet.id, 'name': pet.name}
        pets.append(pet_dict)

    body = {'count': len(pets), 'pets': pets}
    return make_response(body, 200)

# -------------------------
# Run server
# -------------------------
if __name__ == '__main__':
    app.run(port=5555, debug=True)
