from app import app, db
from models.user import User, UserSchema
from models.style import Style, StyleSchema
from models.find import Find, FindSchema
with app.app_context():
    db.drop_all()
    db.create_all()

    user_schema = UserSchema()
    style_schema = StyleSchema()
    find_schema = FindSchema()


    user1 = user_schema.load({
        'email':'loz@gmail.net',
        'age':'41',
        'name':'Lauren'
        })
    
    style1 = style_schema.load({
        'description': 'DIOR OBLIQUE DOWN JACKET - Navy Blue Technical Jacquard',
        'style_image_url': 'https://www.dior.com/couture/ecommerce/media/catalog/product/l/J/1683715469_943C449A4462_C595_E01_ZHC.jpg?imwidth=1080'
        })
    
    find1 = find_schema.load({
        'description': 'UNIQLO ULTRA LIGHT DOWN JACKET - NAVY',
        'find_image_url': 'https://image.uniqlo.com/UQ/ST3/WesternCommon/imagesgoods/460915/item/goods_69_460915.jpg?width=722&impolicy=quality_70&imformat=chrome',
    })
    db.session.add(user1)
    db.session.add(style1)
    db.session.add(find1)
    db.session.commit()
    user_schema.dump(user1)
    style_schema.dump(style1)
    find_schema.dump(find1)
