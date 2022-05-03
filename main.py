import os
import func
import json
from flask import Flask, render_template, request, url_for
import numpy as np

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24).hex()

with open("config.json", "r") as file:
    config = json.load(file)

calculation = []
mode_calculation = "numerical culation"

@app.route("/")
def home():
    return(render_template("main.html", calculation=[], config=config))

@app.route("/", methods=["GET", "POST"])
def redirectCalc():
    value = request.form["menu"]
    if value == "calc":
        return(render_template("calculation.html", calculation=[], config=config))
    if value == "graph":
        return(render_template("main.html", config=config))
    if value == "program":
        return(render_template("main.html", config=config))
    if value == "settings":
        return(render_template("settings.html", config=config))
    else:
        return(render_template("main.html", config=config))

@app.route("/submit", methods=["GET", "POST"])
def submit():
    value = request.form["text"]
    result, resultType = func.calculate(value)
    result = str(result)

    if resultType == "clear":
        calculation.clear()
        
    else:
        try:
            func.ans = float(result)
            func.history.append((value,float(result)))
        except:
            print("ans not supported")
        print(calculation)
        calculation.insert(0, {
            "calculation": (value, result),
            "type": resultType,
            "graphNumber": str(len(os.listdir("static/graphs"))) if resultType == "graph" else None
        })
    return(render_template("calculation.html", calculation=calculation, config=config))


if __name__ == "__main__":
    app.run(debug=True)
