# there are going to be many repipes per user. When pulling recpies from my sql you will be creating a python class using that information and include a creator value and define that using a dictionary with in the same for loop. See assosiating users in classes.
from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.User_model import User
from flask_app.models.Recipe_models import Recipes

@app.route('/recipes')
def show_all_recipe():
    if 'user_id' not in session:
        return redirect('/')
    user_data = {
        'id':session['user_id']
        }
    recipes = Recipes.get_all_with_user()
    print(user_data['id'])
    return render_template('recipes.html', user = User.get_one_user(user_data), all_recipes = recipes)
@app.route('/recipe/<int:recipe_user_id>')
def get_one_recipe(recipe_user_id):
    if 'user_id' not in session:
        return redirect('/')
    user_data = {
        'id':session['user_id']
        }
    return render_template('recipe.html',user = User.get_one_user(user_data), one_recipe = Recipes.get_one_recipe(recipe_user_id))
@app.route('/recipe/new')
def new_recipe():
    if 'user_id' not in session:
        return redirect('/')
    id = {'id':session['user_id']}
    return render_template('new_recipe.html', user = User.get_one_user(id))
@app.route('/recipe/create', methods = ['POST'])
def create_new_recipe():
    if 'user_id' not in session:
        return redirect('/')
    print(request.form)
    id = {'id':session['user_id']}
    Recipes.create_recipe(request.form, id)
    return redirect('/recipes')
@app.route('/delete/<int:recipe_id>')
def delete_recipe(recipe_id):
    if 'user_id' not in session:
        return redirect('/')
    # id = {'id':recipe_id}
    Recipes.delete_user_recipe(recipe_id)
    return redirect('/recipes')
@app.route('/recipe/edit/<int:recipe_id>')
def edit_recipe(recipe_id):
    if 'user_id' not in session:
        return redirect('/')
    id = {'id':session['user_id']}
    print(id)
    return render_template("edit.html", user = User.get_one_user(id), recipe = Recipes.get_one_recipe(recipe_id))
@app.route('/recipe/update/<int:recipe_id>', methods = ['POST']) 
def update_recipe(recipe_id):
    if 'user_id' not in session:
        return redirect('/')
    recipe = {
        'id': recipe_id,
        'user_id':session['user_id'],
        'under_30_min': request.form['under_30_min'],
        'title':request.form['title'],
        'description': request.form['description'],
        'instructions': request.form['instructions']
    }
    Recipes.update_user_recipe(recipe)
    return redirect(f"/recipe/{recipe['id']}")