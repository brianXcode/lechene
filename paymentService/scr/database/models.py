from datetime import datetime
from .db import db 


class Payment(db.Document):
    CURRENCY = (
        ("naira", "naira"),
        ("dollars", "dollars"),
        ("pounds", "pounds"),
        ("euros", "euros")
    )

    STATUS = (
        ("successful", "successful"),
        ("pending", "pending"),
        ("failed", "failed")
    )

    MODE = (
        ("cash", "cash"),
        ("transfer", "transfer"),
        ("bitcoin", "bitcoin")
    )

    payment_mode = db.StringField( max_length=50, required=True, choices=MODE, default="naira" )
    currency = db.StringField( max_length=50, required=True, choices=CURRENCY, default="naira" )
    transaction_status = db.StringField(max_length=30, required=True, choices=STATUS, default="successful")
    amount_paid = db.IntField()
    created_at = db.DateTimeField(auto_now_add=True, default=datetime.now)

    meta = {
        "ordering" : ["-created_at"]
    }


class Delivery(db.Document):

    DELIVERY_STATUS = (
        ("delivered", "delivered"),
        ("pending", "pending"),
        ("failed", "failed")
    )

    ordered_id = db.StringField( max_length=500, required=True)
    delivery_staff_name = db.StringField( max_length=500, required=True)
    location = db.StringField( max_length=1000, required=True)
    status = db.StringField(max_length=30, required=True, choices=DELIVERY_STATUS, default="successful")
    status_report = db.StringField(max_length=1000, required=False, null=True)
    delivered_at = db.DateTimeField(auto_now_add=True, default=datetime.now)

    meta = {
        "ordering" : ["-delivered_at"]
    }

