from flask import Flask
from flask_restx import Api, Resource, fields


app = Flask(__name__)
api = Api(app, title="Users")
