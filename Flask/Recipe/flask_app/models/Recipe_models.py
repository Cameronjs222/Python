from flask_app.config.mySQLconnection import connectToMySQL
from flask_app.models import User_model
from flask import flash


class Recipes:
    my_db = 'recipe'
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.description = data['description']
        self.under_30_min = data['under_30_min']
        self.instructions = data['instructions']
        self.creator = ''
    @classmethod
    def get_all_with_user(cls):
        query = "SELECT * FROM recipes JOIN users ON recipes.users_id = users.id"
        results = connectToMySQL(cls.my_db).query_db(query)
        all_recipes = []
        for results[0] in results:
            recipe = cls(results[0])
            recipe_author = {
                'id':results[0]['users.id'],
                'first_name': results[0]['first_name'],
                'last_name': results[0]['last_name'],
                'email': results[0]['email'],
                'password': results[0]['password'],
                'created_at': results[0]['created_at'],
                'updated_at': results[0]['updated_at']
            }
            author = User_model.User(recipe_author)
            recipe.creator = author
            all_recipes.append(recipe)
        return all_recipes
    @classmethod
    def create_recipe(cls, form_data, id):
        query = """
        INSERT INTO recipes (users_id, title, description, under_30_min, instructions) VALUES (%(users_id)s,%(title)s,%(description)s,%(under_30_min)s,%(instructions)s)
        """
        data = {
            'users_id':id['id'],
            'title': form_data['title'],
            'description':form_data['description'],
            'under_30_min': form_data['under_30_min'],
            'instructions': form_data['instructions']
            }
        
        return connectToMySQL(cls.my_db).query_db(query, data)
    @classmethod
    def get_one_recipe(cls, id):
        query='''SELECT * FROM recipes JOIN users ON recipes.users_id = users.id WHERE recipes.id =  %(id)s'''
        id = {'id':id}
        results= connectToMySQL(cls.my_db).query_db(query, id)
        print(results)
        new_recipe = cls(results[0])
        recipe_author = {
                'id':results[0]['users.id'],
                'first_name': results[0]['first_name'],
                'last_name': results[0]['last_name'],
                'email': results[0]['email'],
                'password': results[0]['password'],
                'created_at': results[0]['created_at'],
                'updated_at': results[0]['updated_at']
            }
        new_recipe.creator = User_model.User(recipe_author)
        return new_recipe
    @classmethod
    def update_user_recipe(cls, form_data):
        query = """
        UPDATE recipes SET title = %(title)s, description = %(description)s, under_30_min = %(under_30_min)s, instructions = %(instructions)s;
        """
        data = {
            'title': form_data['title'],
            'description': form_data['description'],
            'under_30_min': form_data['under_30_min'],
            'instructions': form_data['instructions']
            }
        return connectToMySQL(cls.my_db).query_db(query, data)
    @classmethod
    def delete_user_recipe(cls, form_data):
        query = "DELETE FROM recipes where (id=%(id)s)"
        data = {'id' : form_data}
        return connectToMySQL(cls.my_db).query_db(query, data)
    @staticmethod
    def validation(form_data):
        is_valid = True
        if len(form_data['title']) < 3:
            flash('title must be at least 3 characters long')
            is_valid = False
        if len(form_data['description'])< 3:
            flash('description must be at least 3 characters long')
            is_valid = False
        if len(form_data['instructions'])< 3:
            flash('description must be at least 3 characters long')
            is_valid = False
        return is_valid