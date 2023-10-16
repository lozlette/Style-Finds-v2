# from datetime import datetime
from app import app, ma, db


class User(db.Model):

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)
    name = db.Column(db.String)
    age = db.Column(db.Integer)
    # date_created = db.Column(datetime, auto_now_add=True)


class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User
        fields = ("email", "age", "name")
        load_instance = True

user_schema = UserSchema()
users_schema = UserSchema(many=True)