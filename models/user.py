# from datetime import datetime
from app import app, ma, db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)
    name = db.Column(db.String)
    age = db.Column(db.Integer)


class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        fields = ("email", "age")

user_schema = UserSchema()
users_schema = UserSchema(many=True)