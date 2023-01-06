from flask import Flask, request
from scr.database.db import initialize_db
from scr.urls.routes import initialize_routes
from flask_restful import Api
import requests


app = Flask(__name__)
api = Api(app) 


app.config["MONGODB_SETTINGS"] = MONGO_URI= {
    "db": "order-Service-db",
    "host": "localhost",
    "port": 27017
}


initialize_db(app)
initialize_routes(api)





if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)