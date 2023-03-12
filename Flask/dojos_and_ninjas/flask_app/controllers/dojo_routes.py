from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.user_model import User
from flask_app.models.dojo_model import Dojo


@app.route('/dojos')
def display_dojos():
    results = Dojo.get_all()
    return render_template('dojos.html', dojos=results)

@app.route("/new-dojo", methods = ['POST'])
def add_dojo():
    Dojo.create_new(request.form['new_dojo'])
    return redirect('/dojos')