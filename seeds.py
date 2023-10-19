from app import app, db
from models.user import User, UserSchema
from models.style import Style, StyleSchema
with app.app_context():
    db.drop_all()
    db.create_all()

    user_schema = UserSchema()
    style_schema = StyleSchema()


    user1 = user_schema.load({
        'email':'loz@gmail.net',
        'age':'40',
        'name':'Lauren'
        })
    
    style1 = style_schema.load({
        'description': 'DIOR OBLIQUE DOWN JACKET - Navy Blue Technical Jacquard',
        'style_image_url': 'https://www.dior.com/couture/ecommerce/media/catalog/product/l/J/1683715469_943C449A4462_C595_E01_ZHC.jpg?imwidth=1080'
        })
    
    db.session.add(user1)
    db.session.add(style1)
    db.session.commit()
    user_schema.dump(user1)
    style_schema.dump(style1)
