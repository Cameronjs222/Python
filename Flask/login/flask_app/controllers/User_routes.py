from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.User_model import User

@app.route('/')
def login_reg():
    return render_template('index.html')
@app.route('/user/create', methods=['POST'])
def create_new_user():
    if not User.validation_registration(request.form): #checks if the entered information passes all of the validation specifications.
        return redirect('/')
    new_user = User.create_user(request.form) #creates variable for new user that will be saved in session
    session['user_id'] = new_user
    print(session['user_id'])
    return redirect('/loged-in')
@app.route('/user/login', methods=['POST'])
def validate_login():
    if not User.validation_login(request.form):
        return redirect('/')
    email_data={
        'email':request.form['email']
    }
    returning_user = User.check_email(email_data)
    session['user_id'] = returning_user.id
    return redirect('/loged-in')

@app.route('/loged-in')
def welcome():
    if 'user_id' not in session:
        return redirect('/')
    user_data = {
        'id':session['user_id']
    }
    user = User.get_one_user(user_data)
    return render_template('logged_in.html', user = user)
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
