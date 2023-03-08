from flask import Flask, render_template, request, redirect, session
from user import User
app = Flask(__name__)
app.secret_key = "I'm going to be king of the pirates!"
@app.route('/')
def form():
    return render_template("index.html")
@app.route('/users/create', methods=["POST"])
def create_one():
    print(request.form)
    data = {
    'first_name':request.form['first_name'],
    'last_name':request.form['last_name'],
    'email':request.form['email']
    }
    User.create_one(data)
    return redirect('/users')
@app.route('/users')
def users():
    results = User.get_all()
    return render_template('users.html', users = results)
@app.route('/users/delete/<int:user_id>')
def delete_one(user_id):
    User.delete_one(user_id)
    return redirect("/users")
@app.route('/users/update/<int:user_id>')
def update_one(user_id):
    User.update_one(user_id)
    return redirect('/users')
@app.route('/users/update/edit')
def edit():
    return render_template('edit.html')
@app.route('/users/user/<int:user_id>')
def user(user_id):
    results = User.get_one
    (user_id)
    return render_template('edit.html', user = results)
if __name__ == "__main__":
    app.run(debug=True)