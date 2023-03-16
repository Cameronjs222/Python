from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.User_model import User
# from flask_app.models.Recipe_models import Recipe

@app.route('/')
def login_reg():
    return render_template('index.html')
@app.route('/user/create', methods=['POST'])
def create_new_user():
    if not User.validation(request.form): #checks if the entered information passes all of the validation specifications.
        return redirect('/')
    new_user = User.create_user(request.form) #creates variable for new user that will be saved in session
    print(new_user)
    session['new_user'] = new_user
    return redirect('/post')
@app.route('/post')
def show_all_post():
    return render_template('recipes.html')