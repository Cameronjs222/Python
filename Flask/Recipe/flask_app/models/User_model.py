from flask_app.config.mySQLconnection import connectToMySQL

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
    @staticmethod
    def validation(data):
        pass
