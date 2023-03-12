from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.user_model import User

@app.route('/')
def form():
    return render_template("index.html")
@app.route('/users/create', methods=["POST"])
def create_one():
    print(request.form)
    data = {
    'first_name':request.form['first_name'],
    'last_name':request.form['last_name'],
    'email':request.form['email']
    }
    User.create_one(data)
    return redirect('/users')
@app.route('/users')
def users():
    results = User.get_all()
    return render_template('users.html', users = results)
@app.route('/users/delete/<int:user_id>')
def delete_one(user_id):
    User.delete_one(user_id)
    return redirect("/users")
@app.route('/users/update/<int:user_id>/<string:first_name>/<string:last_name>/<string:email>', methods=['get', 'post'])
def update_one(user_id, first_name, last_name, email):
    print(request.method)
    if request.method == 'GET':
        data = {
        'first_name':first_name,
        'last_name':last_name,
        'email': email,
        'id': user_id
    }
    elif request.method == 'POST':
        data = {
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'email':request.form['email'],
        'id': user_id
    }
    print(request.method)
    User.update_one(data)
    return redirect('/users')
@app.route('/users/update/edit/<int:user_id>/<string:first_name>/<string:last_name>/<string:email>', methods=['get', 'post'])
def edit(user_id,first_name,last_name,email):
    return render_template('edit.html', id=user_id,first_name=first_name,last_name=last_name,email=email)
@app.route('/users/user/<int:user_id>')
def user(user_id):
    user_id = user_id
    print(user_id)
    results = User.get_one(user_id)
    return render_template('user.html', user = results, id=user_id)