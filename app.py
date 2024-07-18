"""
Clase App.
"""
import os
from flask import Flask, request, render_template, redirect, url_for
from flask_restful import Api
from dotenv import load_dotenv
from db import db
from flask_login import LoginManager, login_required, login_user, current_user
from controllers.saludo_controller import SaludoController
from controllers.perros_controller import PerrosController
from models.usuarios import Usuarios

load_dotenv()

secret_key = os.urandom(24)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = (f'mysql'
                                         f'://{os.getenv("USER_DB")}'
                                         f':{os.getenv("PASSWORD_DB")}'
                                         f'@{os.getenv("HOST_DB")}'
                                         f':{os.getenv("HOST_PORT")}'
                                         f'/{os.getenv("SCHEMA_DB")}')
app.config["SECRET_KEY"] = secret_key
db.init_app(app)
api = Api(app)
login_manager = LoginManager(app)


@login_manager.user_loader
def load_user(user_id):
    user = Usuarios.query.get(user_id)
    if user:
        return user
    return None


@app.route("/")
def main():
    return "Bienvenidos..."


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        username = request.form['username']
        password = request.form['password']
        user = Usuarios.query.filter_by(username=username, password=password).first()
        if user:
            login_user(user)
            if user.is_admin:
                return redirect(url_for("perroscontroller"))
            else:
                return redirect(url_for("saludocontroller"))

    return render_template("login.html")


api.add_resource(PerrosController, '/perros')
api.add_resource(SaludoController, '/saludo')
