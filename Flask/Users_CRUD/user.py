from mySQLconnection import connectToMySQL

class User:
    my_db = "users_schema"
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at=  data['created_at']
        self.updated_at = data['updated_at']
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('users_schema').query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        info = {'id':data}
        results = connectToMySQL('users_schema').query_db(query, info)
        users = []
        for user in results:
            users.append(cls(user))
        return users
    @classmethod
    def create_one(cls, data):
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s)"
        return connectToMySQL('users_schema').query_db(query, data)
    @classmethod
    def delete_one(cls, data):
        query = "DELETE FROM users where (id=%(id)s)"
        info = {'id' : data}
        return connectToMySQL('users_schema').query_db(query, info)
    @classmethod
    def update_one(cls,data):
        query = "UPDATE users SET first_name=%(first_name)s,last_name=%(last_name)s, email=%(email)s WHERE id = %(id)s"
        info = {'id' : data}
        return connectToMySQL('users_schema').query_db(query, info)