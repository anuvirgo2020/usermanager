from flask import Flask
from flask_restful import Api
from flask_swagger_ui import get_swaggerui_blueprint
import argparse
import config
from routes import UserRoutes
from db import db

app = Flask(__name__)

parser = argparse.ArgumentParser(description="User Manager API")

parser.add_argument('--db_host', type=str, default='localhost')
parser.add_argument('--db_port', type=int, default=5432)
args = parser.parse_args()

# Configure Database
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{config.DB_USER}:{config.DB_PASSWORD}@{args.db_host}:{args.db_port}/{config.DB_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
api = Api(app)

# Routes
api.add_resource(UserRoutes, '/users', '/users/<int:userid>')


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=9000)
