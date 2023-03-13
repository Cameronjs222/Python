from flask_app.config.mySQLconnection import connectToMySQL

class Dojo:
    my_db = "dojos_and_ninjas"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at=  data['created_at']
        self.updated_at = data['updated_at']
    @classmethod 
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(cls.my_db).query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos
    @classmethod
    def create_new(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s)"
        info = {'name':data}
        return connectToMySQL(cls.my_db).query_db(query, info)
    @classmethod
    def delete_dojo(cls, data):
        query = """
        DELETE FROM dojos WHERE id = %(id)s;
        """
        data = {'id': data}
        return connectToMySQL(cls.my_db).query_db(query, data)
    @classmethod
    def delete_users(cls, data):
        query = "DELETE FROM users where (dojos_id=%(id)s)"
        info = {'id' : data}
        return connectToMySQL(cls.my_db).query_db(query, info)