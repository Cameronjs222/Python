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
    print(request.form['age'])
    data = {
    'first_name':request.form['first_name'],
    'last_name':request.form['last_name'],
    'age':request.form['age'],
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
    return render_template("users.html", users=results, dojo = dojo_id)

# updates

@app.route('/users/update/<int:user_id>/<string:first_name>/<string:last_name>/<string:age>', methods=['get', 'post'])
def update_one(user_id, first_name, last_name, age):
    print(request.method)
    if request.method == 'GET':
        data = {
        'first_name':first_name,
        'last_name':last_name,
        'age': age,
        'id': user_id
    }
    elif request.method == 'POST':
        data = {
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'age':request.form['age'],
        'id': user_id
    }
    print(request.method)
    User.update_one(data)
    return redirect('/dojos')
@app.route('/users/update/edit/<int:user_id>/<string:first_name>/<string:last_name>/<string:age>', methods=['get', 'post'])
def edit(user_id,first_name,last_name,age):
    return render_template('edit.html', id=user_id,first_name=first_name,last_name=last_name,age=age)

# delete

@app.route('/users/delete/<int:user_id>')
def delete_one(user_id):
    print(user_id)
    User.delete_one(user_id)
    return redirect("/dojos")