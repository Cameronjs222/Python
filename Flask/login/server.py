from flask_app import app
from flask_app.controllers import User_routes

if __name__=="__main__":
    app.run(debug=True, port=5000)