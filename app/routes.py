from app import app,api
from flask import request,render_template
from flask_jsonpify import jsonify
from flask_restful import Api, Resource
from random import random,shuffle

class build_list(Resource):
    def get(self):
        # Get users from request
        users = request.args.get('users').split(",")
        # Randomize users
        shuffle(users)
        # Find midpoint
        midpoint = len(users)//2
        # Split teams at the midpoint
        teams = (users[0:midpoint],users[midpoint:len(users)])

        #return the result
        return jsonify(teams)

#The one and only list teams API call
api.add_resource(build_list, "/list")

# Default Route and team route
@app.route('/')
@app.route('/team')
def team():
    return render_template("team.html")

