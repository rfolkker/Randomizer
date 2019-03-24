from flask import Flask
from flask_jsonpify import jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

from app import routes

