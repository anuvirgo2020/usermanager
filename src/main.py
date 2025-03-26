from flask import Flask
from flask_restful import Api
from routes import UserRoutes
import config.dbconfig
import argparse
from db import db
app = Flask(__name__)

parser = argparse.ArgumentParser(description="User Manager API")

parser.add_argument('--db_host', type=str, default='localhost')
parser.add_argument('--db_port', type=int, default=5432)
args = parser.parse_args()

# postgresql://admin:password@localhost:5432/usermanager
app.config['SQLALCHEMY_DATABASE_URI']= f'postgresql://{config.dbconfig.DB_USER}:{config.dbconfig.DB_PASSWORD}@{args.db_host}:{args.db_port}/{config.dbconfig.DB_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
api = Api(app)

# Routes
api.add_resources(UserRoutes, '/users', '/users/<int:userid>')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=9000)