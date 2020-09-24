from src.app import app
from flask import request, Response
from src.helpers.json_response import asJsonResponse
from src.database import db



@app.route("/student/all")
@asJsonResponse

def search_students():
    """display all Ironhack users from datamad0820"""

    students = db.users.find({}, {'_id': False})

    return students