from database import SessionLocal
from models import AIModel

db = SessionLocal()

try:
    models = db.query(AIModel).all()#this is querry to get all the models from the database

    for model in models:
        print(
            model.id,
            model.name,
            model.provider
        )

finally:
    db.close()