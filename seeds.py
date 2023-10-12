from app import app, db, bcrypt
from models.user import User, UserSchema
with app.app_context():
    db.drop_all()
    db.create_all()

    user_schema = UserSchema()

    user1 = User(email="loz@gmail.net", age=40, name="Lauren")
    
    db.session.add(user1)
    db.session.commit()
    user_schema.dump(user1)
