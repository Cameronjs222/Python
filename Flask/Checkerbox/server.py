from flask import Flask, render_template
app = Flask(__name__)
def box(rows, boxs, color_1, color_2):
    return render_template("index.html", rows=rows, boxs=boxs,color_1=color_1, color_2=color_2, width=100*boxs)
@app.route("/")
def route1():
    return box()
@app.route("/hello")
def route2():
    return box()
@app.route("/<int:num1>/<int:num2>/<string:color1>/<string:color2>")
def route_end(num1, num2, color1, color2):
    return box(int(num1/2) + (num1 % 2 > 0), int(num2/2) + (num1 % 2 > 0), color1, color2,)
if __name__ == "__main__":
    app.run(debug=True)