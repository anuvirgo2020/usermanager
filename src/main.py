from flask import Flask
from flask_restful import Api
from flask_swagger_ui import get_swaggerui_blueprint
import argparse

app = Flask(__name__)

parser = argparse.ArgumentParser(description="User Manager API")

parser.add_argument('--db_host', type=str, default='localhost')
parser.add_argument('--db_port', type=int, default=5432)
args = parser.parse_args()

api = Api(app)

# Routes
api.add_resources(UserRoutes, 'users', '/users/<int:userid>')

app.run(host="0.0.0.0", port=9000)