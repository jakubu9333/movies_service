from app import db, app, seed


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        seed("seed.json")
