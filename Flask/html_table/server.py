from flask import Flask
app = Flask(__name__)
users = [
   {'first_name' : 'Michael', 'last_name' : 'Choi'},
   {'first_name' : 'John', 'last_name' : 'Supsupin'},
   {'first_name' : 'Mark', 'last_name' : 'Guillen'},
   {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
@app.route("/")
def route1():
   return "hello world"
if __name__ == "__main__":
    app.run(debug=True)