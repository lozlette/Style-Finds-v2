from app import app, ma, db

class Style(db.Model):

     __tablename__ = "styles"
     id = db.Column(db.Integer, primary_key=True)
     description = db.Column(db.String)
     style_image_url = db.Column(db.String)
     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


class StyleSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Style
        fields = ("id", "description", "style_image_url", "user_id")
        load_instance = True

style_schema = StyleSchema()
styles_schema = StyleSchema(many=True)