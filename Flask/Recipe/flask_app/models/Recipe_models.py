from flask_app.config.mySQLconnection import connectToMySQL
from flask_app.models import User_model

class Recipes:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.description = data['description']
        self.under_30_min = data['under_30_min']
        self.instructions = data['instructions']
        self.creator = None
    @classmethod
    def get_all_with_user():
        pass
    @classmethod
    def create_recipe():
        pass
    @classmethod
    def get_one_recipe():
        pass
    @classmethod
    def update_user_recipe():
        pass
    @classmethod
    def delete_user_recipe():
        pass
