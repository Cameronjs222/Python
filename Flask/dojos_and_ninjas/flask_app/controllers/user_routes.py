from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.user_model import User
from flask_app.models.dojo_model import Dojo

@app.route('/')
def form():
    dojos = Dojo.get_all()
    dojos_len = len(dojos)
    return render_template("index.html", dojos=dojos, dojos_len=dojos_len)
@app.route('/users/create', methods=["POST"])
def create_one():
    print(request.form)
    data = {
    'first_name':request.form['first_name'],
    'last_name':request.form['last_name'],
    'email':request.form['email'],
    'dojos_id': request.form['dojo']
    }
    User.create_one(data)
    return redirect('/dojos')
@app.route('/users')
def users():
    results = User.get_all()
    dojos = Dojo.get_all()
    print(dojos[0].id)
    return render_template('users.html', users = results, dojos = dojos)
@app.route('/users/<int:dojo_id>')
def dojo_users(dojo_id):
    results = User.get_all(dojo_id)
    return render_template("users.html", users=results)