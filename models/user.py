from your_orm import Model, Column, Integer, String, DateTime

class User(Model):
    email = Column(String)
    name = Column(String)
    age = Column(Integer)
    date_created = Column(DateTime, auto_now_add=True)


class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        fields = ("email", "date_created")

user_schema = UserSchema()
users_schema = UserSchema(many=True)