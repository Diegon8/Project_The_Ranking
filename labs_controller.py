from src.app import app
from flask import request, Response
from src.helpers.json_response import asJsonResponse
from src.database import db
import json
from bson.json_util import dumps



@app.route("/lab/create/")
@app.route("/lab/create/<labname>")
def createLab(labname=None):
        
    query = {"title": labname}

    if db.pulls.find_one(query):
        data = dumps({"Error": "This lab already exists"})
        return Response(data, status=409, mimetype='application/json')

    else:
        data = dumps(db.pulls.insert_one({"lab": labname}).inserted_id)
        return Response(data, status=200, mimetype='application/json')
