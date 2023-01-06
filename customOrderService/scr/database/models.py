from datetime import datetime
from .db import db 


GENDER = (
        ("male", "male"),
        ("female", "female"),
        ("others", "others")
    )

class CustomOrder(db.Document):
    product_category_id = db.StringField( max_length=100, required=True)
    product_SubCategory_id = db.StringField( max_length=100, required=True)
    gender = db.StringField(max_length=50, choices=GENDER, required=True)
    sizes = db.StringField( max_length=100, required=True)
    created_at = db.DateTimeField(auto_now_add=True, default=datetime.now)



class Measurement(db.Document):
    custom_order_id = db.StringField( max_length=100, required=True, null=True)
    gender = db.StringField(max_length=50, choices=GENDER, required=True)
    shoulder = db.IntField()
    hand_length = db.IntField()
    chest_bust = db.IntField()
    stomach = db.IntField()
    top_lenght = db.IntField()
    round_arm = db.IntField() 
    waist = db.IntField() 
    tigh = db.IntField() 
    knee = db.IntField() 
    around_leg = db.IntField()
    leg_length = db.IntField() 
    sizes = db.IntField() 
    other_info = db.StringField( max_length=1000, required=False, null=True)
    created_at = db.DateTimeField(auto_now_add=True, default=datetime.now)