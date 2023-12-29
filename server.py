import os
from flask import Flask
from flask_restful import Resource, Api

app = Flask(name)
api = Api(app)

class Greeting (Resource):
    def get(self):
        return "Auto-Approve is running !"

api.add_resource(Greeting, '/')
app.run(host="52.41.36.82", port=os.environ.get("PORT", 8080))
