from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def hello():
    return render_template("index.html")
@app.route('/play')
def squares():
    return render_template("play.html", amount = 3, version = "teal")
@app.route('/play/<int:num>')
def playground_squares_num(num):
        return render_template("play.html", amount=num, version = "teal")
@app.route('/play/<int:num>/<string:color>')
def playground_squares_num_color(num, color):
    return render_template("play.html", amount=num, version=color)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
