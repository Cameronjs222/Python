from flask import Flask, render_template, request, redirect
from user import User
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/users")
def users():
    users = User.get_all()
    print(users)
    return render_template("users.html", users=users)
@app.route('/create_user', methods=["POST"])
def create_user():
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "mail" : request.form["mail"]
    }
    # for i in data:
    #     if data[i] == "":
    #         data.pop(data[i])
    # print(data)
    User.save(data)
    return redirect('/users')
if __name__ == "__main__":
    app.run(debug=True)

