from models import db, Pet
from app import app

with app.app_context():
    db.create_all()  # ensure tables exist

    # Clear existing data
    Pet.query.delete()

    pets = [
        Pet(name="Robin", species="Hamster"),
        Pet(name="Gwendolyn", species="Dog"),
        Pet(name="Michael", species="Turtle"),
        Pet(name="Austin", species="Cat"),
        Pet(name="Jennifer", species="Dog"),
        Pet(name="Jenna", species="Dog"),
        Pet(name="Crystal", species="Chicken"),
        Pet(name="Jacob", species="Cat"),
        Pet(name="Nicole", species="Chicken"),
        Pet(name="Trevor", species="Turtle"),
    ]

    db.session.add_all(pets)
    db.session.commit()
    print("Seeded 10 random pets!")
