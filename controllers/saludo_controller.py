from flask import render_template, make_response
from flask_restful import Resource

"""
Clase SaludoController.
"""


class SaludoController(Resource):

    def get(self):
        return make_response(render_template("saludo.html"))
