from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes
@app.route('/')
def count():
    if "visits" not in session:
        session["visits"] = 0
    else:
        session["visits"] += 1
    return render_template("index.html")

@app.route('/delete')
def delete():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
