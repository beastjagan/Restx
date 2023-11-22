from rest_framework import api, Resource
from database import select, session
from database.UsersModel import User, user_schema


ns = api.namespace("user")

@ns.route("/")
class UsersList(Resource):
    @session
    @ns.marshal_list_with(user_schema)
    def get(self):
        users = select(i for i in User)
        users = [i for i in users]
        return users
  