from flask import Flask, render_template, request
import utils

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/result")
def result(method="POST"):
    return render_template("result.html", q=request.form["input"], result=getResult(q))
