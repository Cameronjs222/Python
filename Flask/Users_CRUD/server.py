from flask import Flask, render_template, request, redirect, session
from user import User
app = Flask(__name__)
app.secret_key = "I'm going to be king of the pirates!"
@app.route('/')
def add_one():
    return render_template("index.html")
app.route('/users/delete/<int:user_id>')
def delete_one(user_id):
    User.delete_one(user_id)
    return redirect("/")
if __name__ == "__main__":
    app.run(debug=True)