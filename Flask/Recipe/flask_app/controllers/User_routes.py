from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.User_model import User
# from flask_app.models.Recipe_models import Recipe

@app.route('/')
def login_reg():
    return render_template('index.html')
@app.route('/user/create' methods=['POST'])
def create_new_user():