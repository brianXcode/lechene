from flask import request, render_template, jsonify
from flask_jwt_extended import create_access_token, decode_token
from ..database.models import User
from flask_restful import Resource
import datetime
from jwt.exceptions import ExpiredSignatureError, DecodeError, \
    InvalidTokenError

# from ..mail_services.password_mail import send_email



# class ForgotPassword(Resource):

#     def post(self):
#         url = request.host_url + "reset/"
#         try:
#             body = request.get_json()
#             email = body.get("email")

#             if not email:
#                 return jsonify({
#                     "message":"wrong Email"
#                 })

#             user = User.objects.get(email=email)
#             if not user:
#                 return jsonify({
#                     "message":"email does not exist"
#                 })
            
#             reset_token = create_access_token(
#                 str(user.id), 
#                 expires_delta = datetime.timedelta(days=1)
#             )

#             return send_email(
#                 "Lechene-User-Service",
#                 sender = "support@lechene.com",
#                 receipients = [user.email],
#                 text_body = render_template(
#                     "email/reset_password.txt",
#                     url=url + reset_token
#                 ),
#                 html_body = render_template(
#                     "email/reset_password.html",
#                     url=url + reset_token
#                 )
#             )
#         except:
#             return jsonify({
#                 "message": "something wemt wrong, please provide the correct email"
#             })



# class ResetPassword(Resource):
#     def post(self):
#         url = request.host_url + "reset/"

#         try:
#             body = request.get_json()
#             reset_token = body.get("reset_token")
#             password = body.get("password")

#             if not reset_token or not password:
#                 return jsonify({
#                     "message": "Wrong reset_token or password, please provide the correct one"
#                 })
            
#             user_id = decode_token(reset_token)["identity"]
#             user = User.objects.get(id=user_id)

#             user.modify(password=password)
#             user.hash_password()
#             user.save()

#             return send_email('[Lechene-User-Service] Password reset successful',
#                               sender='support@lechene.com',
#                               recipients=[user.email],
#                               text_body='Password reset was successful',
#                               html_body='<p>Password reset was successful</p>')

        
#         except:
#              return jsonify({
#                 "message": "something wemt wrong, please try again"
#             })
