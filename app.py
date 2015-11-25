from flask import Flask, render_template, request
import utils

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/result", methods = ["POST"])
def result():
    question = request.form["input"]
    return render_template("result.html", q = question, result = utils.getResult(question))


if __name__ == "__main__":
    app.debug = True
    app.run(host = '0.0.0.0', port=8000)
