from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route("/")
def survey():
    return render_template("index.html")
@app.route('/process',methods=['POST'])
def process():
    print("Got Post Info")
    print(request.form)
    return "hello world"
if __name__ == "__main__":
    app.run(debug=True)
