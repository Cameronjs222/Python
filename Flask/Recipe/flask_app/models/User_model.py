from flask_app import app
from flask_app.config.mySQLconnection import connectToMySQL
from flask import flash
import re
from flask_bcrypt import Bcrypt
bcrypt= Bcrypt(app)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# PW_REGEX = #create later

class User:
    my_db='recipe'
    def __init__(self, form_data):
        self.first_name = form_data['first_name']
        self.last_name = form_data['last_name']
        self.email = form_data['email']
        self.password = form_data ['password']
    @classmethod
    def create_user(cls, form_data):
        query = """
        INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(pw_hash)s)
        """
        pw_hash = bcrypt.generate_password_hash(form_data['password'])
        data = {
            "first_name": form_data['first_name'],
            "last_name": form_data['last_name'],
            "email": form_data['email'],
            "password": pw_hash
        }
        results = connectToMySQL(cls.my_db).query_db(query, data)
        return results
    @classmethod
    def get_all(cls, form_data):
        pass #should use join left in order to merge all the data from the recpies table with the users table in order to display all users and their recipes.
    @classmethod
    def update_user_info(cls, form_data):
        pass
    @classmethod
    def delete_user(cls,form_data):
        pass
    @classmethod
    def check_email(cls, form_data):
        query = """
        SELECT * FROM users
        WHERE users.email = %(email)s;
        """
        user_info = {"email": form_data}
        results = connectToMySQL(cls.my_db).query_db(query, user_info)
        print("results")
        print(results)
        if results:
            return True
        else:
            return False
    @staticmethod
    def validation(form_data):
        is_valid = True
        if User.check_email(form_data['email']):
            flash("email entered is already in our system.")
            is_valid = False
        if len(form_data['first_name']) < 3 or len(form_data['last_name']) < 3:
            flash('Name must be at least three characters long.')
            is_valid = False
        if form_data['password_confirmation'] != form_data['password']:
            flash('Passwords must match')
        if not EMAIL_REGEX.match(form_data['email']):
            flash('Invalid user email format')
        return is_valid
