from flask_app import app
from flask_app.config.mySQLconnection import connectToMySQL
from flask import flash
import re
from flask_bcrypt import Bcrypt
bcrypt= Bcrypt(app)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    my_db='login'
    def __init__(self, form_data):
        self.id = form_data['id']
        self.first_name = form_data['first_name']
        self.last_name = form_data['last_name']
        self.email = form_data['email']
        self.password = form_data['password']
        self.created_at = form_data['created_at']
        self.updated_at = form_data['updated_at']
    @classmethod
    def create_user(cls, form_data):
        query = """
        INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s)
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
    def get_one_user(cls, data):
        query = """
        SELECT * FROM users WHERE users.id = %(id)s
        """
        results = connectToMySQL(cls.my_db).query_db(query,data)
        return cls(results[0])
    @classmethod
    def get_all(cls):
        query='''
            SELECT * FROM users
        '''
        results= connectToMySQL(cls.my_db).query_db(query)
        if results:
            users=[]
            for user in results:
                one_user= cls(user)
                users.append(one_user)
                
            return users
        else:
            return None    
    @classmethod
    def update_user_info(cls, form_data):
        query = "UPDATE users SET first_name=%(first_name)s,last_name=%(last_name)s, email=%(email)s WHERE id = %(id)s"
        return connectToMySQL(cls.my_db).query_db(query, form_data)
    @classmethod
    def delete_one(cls, form_data):
        query = "DELETE FROM users where (id=%(id)s)"
        data = {'id' : form_data}
        return connectToMySQL(cls.my_db).query_db(query, data)
    @classmethod
    def check_email(cls, form_data):
        query= '''
            SELECT * FROM users
            WHERE users.email = %(email)s;
        '''
        results= connectToMySQL(cls.my_db).query_db(query, form_data)
        if results:
            user = cls(results[0])
            return user
        else:
            return False
    @staticmethod
    def validation_registration(form_data):
        is_valid = True
        if User.check_email(form_data):
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
    @staticmethod
    def validation_login(form_data):
        is_valid = True
        data= { "email": form_data["email"]}
        valid_user = User.check_email(data)
        if not valid_user:
            flash("Invalid credentials")
            is_valid = False
        if valid_user:
            if not bcrypt.check_password_hash(valid_user.password, form_data['password']):
                flash("Invalid credentials")
                is_valid = False
        return is_valid
