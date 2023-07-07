from app import app, db
from models import User, user, UserSchema, user_schema
from flask import jsonify

with app.test_request_context():
    print(jsonify(user_schema.dump(user)))
    db.create_all()

    user_schema = UserSchema()
    # style_schema = StyleSchema()
    # find_schema = FindSchema()

    user = User(email="loz@gmail.net", age=40, name="Lauren")
    
    db.session.add(user)
    db.session.commit()
    user_schema.dump(user)
