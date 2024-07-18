from flask import render_template, make_response
from flask_restful import Resource
from models.perros import Perros
from flask_login import login_required

"""
Clase PerrosController.
"""


class PerrosController(Resource):

    @login_required
    def get(self):
        items = Perros.query.all()
        return make_response(render_template("perros.html", items=items))
