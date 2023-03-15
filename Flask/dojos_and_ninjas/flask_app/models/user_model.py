from flask_app.config.mySQLconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class User:
    my_db = "dojos_and_ninjas"
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.age = data['age']
        self.created_at=  data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojos_id']
    @classmethod
    def get_all(cls, data=None):
        query = "SELECT * FROM users WHERE dojos_id=%(dojos_id)s;"
        data = {'dojos_id':data}
        results = connectToMySQL(cls.my_db).query_db(query, data)
        print(results)
        users = []
        for user in results:
            users.append(cls(user))
        return users
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        info = {'id':data}
        results = connectToMySQL(cls.my_db).query_db(query, info)
        # users = []
        # for user in results:
        #     users.append(cls(user))
        print(results)
        return cls(results)
    @classmethod
    def create_one(cls, data):
        query = "INSERT INTO users (first_name, last_name, age, dojos_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojos_id)s)"
        return connectToMySQL(cls.my_db).query_db(query, data)
    @classmethod
    def delete_one(cls, data):
        query = "DELETE FROM users where (id=%(id)s)"
        info = {'id' : data}
        return connectToMySQL(cls.my_db).query_db(query, info)
    @classmethod
    def update_one(cls,data):
        query = "UPDATE users SET first_name=%(first_name)s,last_name=%(last_name)s, age=%(age)s WHERE id = %(id)s"
        return connectToMySQL(cls.my_db).query_db(query, data)
    @classmethod
    def delete_one(cls, data):
        query = "DELETE FROM users where (id=%(id)s)"
        info = {'id' : data}
        return connectToMySQL(cls.my_db).query_db(query, info)
    
    # validation
    @staticmethod
    def validation(data):
        is_valid = True
        # added or so that users will only get one error message if both first and last name are under 3 characters
        if len(data['first_name']) < 3 or len(data['last_name']) < 3:
            flash('Name must be at least three characters long.')
            is_valid = False
        if  str(data['age']):
            flash('age must be a number')
            is_valid
        if int(data['age']) > 120:
            flash('Age entered is to large.')
            is_valid = False
        if int(data['age']) < 12:
            flash('Users must be at least 12 years old before registering.')
            is_valid = False
        if not EMAIL_REGEX.match(data['email']):
            flash('Invalid user email')
        return is_valid


