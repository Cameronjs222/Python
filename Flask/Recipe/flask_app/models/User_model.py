from flask_app.config.mySQLconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    my_db='recipe'
    def __init__(self, data):
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data ['password']
    @classmethod
    def create_user(cls, data):
        pass #should check if email is already entered into our system here
    @classmethod
    def get_all(cls, data):
        pass #should use join left in order to merge all the data from the recpies table with the users table in order to display all users and their recipes.
    @classmethod
    def update_user_info(cls, data):
        pass
    @classmethod
    def delete_user(cls,data):
        pass
    @classmethod
    def check_email(cls, data):
        query = """
        SELECT * FROM users
        WHERE users.email = %(email)s;
        """
        user_info = {"email": data}
        results = connectToMySQL(cls.my_db).query_db(query, user_info)
        print("results")
        print(results)
        if results:
            return True
        else:
            return False
    @staticmethod
    def validation(data):
        is_valid = True
        if User.check_email(data['email']):
            flash("email entered is already in our system.")
            is_valid = False
        if len(data['first_name']) < 3 or len(data['last_name']) < 3:
            flash('Name must be at least three characters long.')
            is_valid = False
        if not EMAIL_REGEX.match(data['email']):
            flash('Invalid user email format')
        return is_valid
