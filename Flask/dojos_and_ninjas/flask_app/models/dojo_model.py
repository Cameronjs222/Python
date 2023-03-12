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
        print(dojos[0].name)
        return dojos