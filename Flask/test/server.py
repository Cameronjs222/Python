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
    session['Name'] = request.form['name']
    session['Location'] = request.form['location']
    session['Language'] = request.form['language']
    session['Comments'] = request.form['comment']
    return redirect('/display')
@app.route('/display')
def display():
    return render_template('display.html', Name = 'Name')
@app.route('/delete')
def delete():
    session.clear()
    return redirect('/')
if __name__ == "__main__":
    app.run(debug=True)
