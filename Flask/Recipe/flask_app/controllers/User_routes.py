from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.User_model import User
# from flask_app.models.Recipe_models import Recipe

@app.route('/')
def login_reg():
    return render_template('index.html')
@app.route('/user/create', methods=['POST'])
def create_new_user():
    print(request.form)
    if not User.validation_registration(request.form): #checks if the entered information passes all of the validation specifications.
        return redirect('/')
    new_user = User.create_user(request.form) #creates variable for new user that will be saved in session
    print(new_user)
    session['user_id'] = new_user
    print(session['user_id'])
    return redirect('/post')
@app.route('/user/login', methods=['POST'])
def validate_login():
    if not User.validation_login(request.form):
        return redirect('/')
    print("validated")
    email_data={
        'email':request.form['email']
    }
    returning_user = User.check_email(email_data)
    session['user_id'] = returning_user.id
    return redirect('/post')

@app.route('/post')
def show_all_post():
    user_id=session['user_id']
    return render_template('recipes.html', id= user_id)