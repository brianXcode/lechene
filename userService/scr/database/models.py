from datetime import datetime
from .db import db 
from flask_bcrypt import generate_password_hash, check_password_hash




class User(db.Document):
    ROLES = (
        ('admin', 'admin'),
        ('staff', 'staff'),
        ('tailor', 'tailor'),
        ("visitor", "visitor")
    )
   
    username = db.StringField(required=True, )
    password = db.StringField(required=True, min_length=6)
    email = db.EmailField(required=True, unique=True)
    roles = db.StringField(max_length=50, choices=ROLES,  required=False)
    created_at = db.DateTimeField(auto_now_add=True, default=datetime.now)
    active = db.BooleanField(default=True)
    is_admin = db.BooleanField(default=False)
    is_staff = db.BooleanField(default=False)


    def hash_password(self):
        self.password = generate_password_hash(self.password).decode("utf8")
    
    def check_password(self, password):
        return check_password_hash(self.password, password)
        
    meta = {
        "ordering" : ["-created_at"]
    }



class Profile(db.Document):
    user = db.ReferenceField(User, unique=True)
    first_name = db.StringField(max_length=500, required=True)
    last_name = db.StringField(max_length=500, required=True)
    address = db.StringField(max_length=500)
    # image = db.FileField()
    phone_number = db.StringField(max_length=12)
    about = db.StringField(max_length=2000)
    created_at = db.DateTimeField(auto_now_add=True, default=datetime.now)
    active = db.BooleanField(default=False)
    
"""
    This is a delete rules ::
    If a user is deleted from the database,
    then the profile created by that user is also deleted 
"""
User.register_delete_rule(Profile, "added_by", db.CASCADE)

    


    
