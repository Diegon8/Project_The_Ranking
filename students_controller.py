from src.app import app
from flask import request, Response
from src.helpers.json_response import asJsonResponse
from src.database import db
import json
from bson.json_util import dumps



@app.route("/student/all")
@asJsonResponse

def search_students():
    'display all users from datamad0820'

    students = db.users.find({}, {'_id': False})

    return students


@app.route("/student/create/")
@app.route("/student/create/<studentname>")
def createStudent(studentname=None):
        
    query = {"user": studentname}

    if db.pulls.find_one(query):
        data = dumps({"Error": "This user already exists"})
        return Response(data, status=409, mimetype='application/json')

    else:
        data = dumps(db.pulls.insert_one({"user": studentname}).inserted_id)
        return Response(data, status=200, mimetype='application/json')
