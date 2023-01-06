from datetime import datetime
from .db import db 


class OrderProduct(db.Document):
    STATUS = (
        ('pending', 'pending'),
        ('completed', 'completed'),
        ('refunded', 'refunded'),
    )
    
    product_id = db.StringField(required=True)
    price = db.IntField()
    added_fee = db.IntField()
    quantity = db.IntField(required=True)
    status = db.StringField(max_length=50, choices=STATUS, default="PENDING")
    created_at = db.DateTimeField(auto_now_add=True, default=datetime.now)
    

    meta = {
        "ordering" : ["-created_at"]
    }


class Ordered(db.Document):
    order_product_id = db.ListField(db.StringField(), required=True)
    ordered_date = db.DateTimeField(auto_now_add=True, default=datetime.now)
   
    meta = {
        "ordering" : ["-ordered_date"]
    }


class OrderedReview(db.Document):

    RETURN_REQUEST = (
        ('yes', 'yes'),
        ('no', 'no'),
    )

    ordered_id = db.StringField(required=True)
    rating = db.IntField(required=True)
    review = db.StringField(max_length=500, required=False )
    return_request = db.StringField(max_length=10, choices=RETURN_REQUEST, default="no")
    created_at = db.DateTimeField(auto_now_add=True, default=datetime.now)

    meta = {
        "ordering" : ["-created_at"]
    }


