import datetime
from flask import Flask, request, jsonify, Blueprint
from flask_bcrypt import Bcrypt
from flask_restful import Api
from scr.database.db import initialize_db
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from scr.database.models import User
from scr.urls.routes import initialize_routes


app = Flask(__name__)

"""TODO mail server config"""
# MAIL_SERVER = "localhost"
# MAIL_PORT = "1025",
# MAIL_USERNAME = "support@lechene.com"
# MAIL_PASSWORD = ""
# mail = Mail(app)





api = Api(app) 
bcrypt = Bcrypt(app)
initialize_db(app)
initialize_routes(api)


""" jwt configuration """
jwt = JWTManager(app)
app.config['JWT_SECRET_KEY'] = 'Your_Secret_Key'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days=1)



""" database configuration """
app.config["MONGODB_SETTINGS"] = MONGO_URI= {
    "db": "user_service_db",
    "host": "localhost",
    "port": 27017
}




from scr.views.auth import user_api_blueprint
from scr.views.profile import profile_api_blueprint

app.register_blueprint(user_api_blueprint)
app.register_blueprint(profile_api_blueprint)




if __name__ == '__main__':
    app.run(
        debug=True, 
        host='0.0.0.0', 
    
    )
 
