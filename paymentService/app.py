from flask import Flask
from flask_restful import Api
from scr.database.db import initialize_db
from scr.urls.routes import initialize_routes

app = Flask(__name__)
api = Api(app)

app.config["MONGODB_SETTINGS"] = MONGO_URI= {
    "db": "payment-delivery-ServiceDb",
    "host": "localhost",
    "port": 27017
}

initialize_db(app)
initialize_routes(api)


if __name__ == '__main__':
    app.run(debug=True)