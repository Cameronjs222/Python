from flask_app.config.mySQLconnection import connectToMySQL
from flask_app.models import User_model

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
        print(results)
        all_recipes = []
        print("should contain empty list",all_recipes)
        for row in results:
            recipe = cls(row)
            recipe_author = {
                'id':row['users.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'email': row['email'],
                'password': row['password'],
                'created_at': row['created_at'],
                'updated_at': row['updated_at']
            }
            author = User_model.User(recipe_author)
            recipe.creator = author
            all_recipes.append(recipe)
            print("Should contain object in list",all_recipes)
        return all_recipes
    @classmethod
    def create_recipe(cls, form_data):
        query = """
        INSERT INTO recipes (users_id, title, description, under_30_min, instructions) VALUES (%(users_id)s,%(title)s,%(description)s,%(under_30_min)s,%(instructions)s)
        """
        data = {
            'user_id':form_data['user_id'],
            'title': form_data['title'],
            'description':form_data['under_30_min'],
            'under_30_min': form_data['under_30_min'],
            'instructions': form_data['instructions']
            }
        return connectToMySQL(cls.my_db).query_db(query, data)
    @classmethod
    def get_one_recipe(cls, id):
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        data = {'id':id}
        results = connectToMySQL(cls.my_db).query_db(query, data)
        return cls(results[0])
    @classmethod
    def update_user_recipe(cls, form_data):
        query = """
        UPDATE recipes SET title = %(title)s description = %(description)s under_30_min = %(under_30_min)s instructions = %(instructions)s;
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