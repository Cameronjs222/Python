from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')
def hello():
    return render_template("index.html")
@app.route('/repeat/<int:num>/<string:name>')
def repeat(name, num):
    return render_template("hello.html", hello_num = num, hello_name = name)
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
