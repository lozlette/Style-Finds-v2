from app import app, ma, db

class Find(db.Model):

     __tablename__ = "finds"
     id = db.Column(db.Integer, primary_key=True)
     description = db.Column(db.String)
     find_image_url = db.Column(db.String)
     style_id = db.Column(db.Integer, db.ForeignKey('styles.id'))
     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


class FindSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Find
        fields = ("id", "description", "find_image_url", "style_id", "user_id")
        load_instance = True

find_schema = FindSchema()
finds_schema = FindSchema(many=True)