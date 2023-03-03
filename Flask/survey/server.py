from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' 
@app.route("/")
def survey():
    return render_template("index.html")
@app.route('/process',methods=['POST'])
def process():
    print("Got Post Info")
    print(request.form)
    session['user'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/display')
@app.route('/display')
def display():
    return session['user']
if __name__ == "__main__":
    app.run(debug=True)
