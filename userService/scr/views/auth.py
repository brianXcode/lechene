import datetime
import hashlib
from flask import Response, jsonify, request, Blueprint
from flask_restful import Resource 
from ..database.models import User
from flask_jwt_extended import create_access_token, jwt_required




"""
    Registeration and SignIn

"""

class AdminSignUpApi(Resource):
    def post(self):
        body = request.get_json()
        user = User.objects.create(
            username = body["username"],
            password = body["password"],
            email = body["email"],
            roles = "admin",
            is_admin = True,
            is_staff = False
        )

        user.hash_password()
        user.save()
        id = user.id 
        
        return {
            'id': str(id),
            "username": user.username,
            "userType": user.roles,
            "is_admin": user.is_admin
        }, 200

class StaffSignUpApi(Resource):
    def post(self):
            body = request.get_json()
            user = User.objects.create(
                username = body["username"],
                password = body["password"],
                email = body["email"],
                roles = "staff",  
                is_admin = False,
                is_staff = True
            )
    
            user.hash_password()
            user.save()
            id = user.id 
            return {
                'id': str(id),
                "username": user.username,
                "userType": user.roles
            }, 200

class TailorSignUpApi(Resource):
    def post(self):
            body = request.get_json()
            user = User.objects.create(
                username = body["username"],
                password = body["password"],
                email = body["email"],
                roles = "tailor",
                is_admin = False,
                is_staff = False
            )
    
            user.hash_password()
            user.save()
            id = user.id 
            return {
                'id': str(id),
                "username": user.username,
                "userType": user.roles
            }, 200
           
class VisiorSignUpApi(Resource):
    def post(self):
            body = request.get_json()
            user = User.objects.create(
                username = body["username"],
                password = body["password"],
                email = body["email"],
                roles = "visitor" ,
                is_admin = False,
                is_staff = False 
              
            )
          
            user.hash_password()
            user.save()
            id = user.id 
            return{
                'id': str(id),
                "username": user.username,
                "userType": user.roles
            }, 200

class UserSignInApi(Resource):

    def post(self):
        body= request.get_json()
        user = User.objects.get(
            email = body.get("email")
        )

        authorized = user.check_password(
            body.get("password")
        )

        if not authorized:
            return jsonify({
                "error": "Invalid Email or Password"
            }, 401)
      
        access_token = create_access_token(
            identity = str(user.id),
            expires_delta = datetime.timedelta(days=1)
        )

        return {
            'token': access_token
        }, 200



user_api_blueprint = Blueprint("user_api", __name__)





from flask.views import View

class UserList(View):
    
    @user_api_blueprint.route("/api/user", methods=["GET"])
    def get_users():
        users = User.objects.all()
        return jsonify({
            "users":users
        })

    @user_api_blueprint.route("/api/admin_user", methods=["GET"])
    @jwt_required()
    def get_admin_user():
        users = User.objects.filter(
            active=True,
            roles="admin"
        )
        return jsonify({
            "users":users
        })

    @user_api_blueprint.route("/api/visitors", methods=["GET"])
    @jwt_required()
    def get_visitors():
        users = User.objects.filter(
            active=True,
            roles="visitor"
        )
        return jsonify({
            "users":users
        })

    @user_api_blueprint.route('/api/user/<username>/exists', methods=['GET'])
    def get_username(username):
        user = User.objects.filter(username=username).first()
        if user is not None:
            response = jsonify({'result': True})
        else:
            response = jsonify({'message': 'Cannot find username'}), 404
        return response