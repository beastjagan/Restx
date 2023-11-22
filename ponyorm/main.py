
from rest_framework import app, api

from methods.UserMethod import ns as UserNamespace


api.add_namespace(UserNamespace)



if __name__ == "__main__":
    app.run(debug=True)


