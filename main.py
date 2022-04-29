import os
import func
import json
from flask import Flask, render_template, request
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

@app.route("/settings", methods=["GET", "POST"])
def setting():
    value = request.form["menu"]
    if value == "mode_calculation":
        func.mode_calc = (func.mode_calc + 1)%2
        if func.mode_calc == 0:
            mode_calculation = "formal calculation"
        if func.mode_calc == 0:
            mode_calculation = "numerical culation"
        print(func.mode_calc)
        func.importing(func.mode_calc)
        return(render_template("calculation.html", calculation=[], config=config))
    else:
        return(render_template("settings.html", config=config))


@app.route("/submit", methods=["GET", "POST"])
def submit():
    value = request.form["text"]
    result = str(func.calculate(value))
    try:
        func.ans = float(result)
        func.history.append((value,float(result)))
    except:
        print("ans not supported")
    print(func.history)
    calculation.insert(0, (value, result))
    return(render_template("calculation.html", calculation=calculation, config=config))

# https://towardsdatascience.com/using-python-flask-and-ajax-to-pass-information-between-the-client-and-server-90670c64d688
# https://www.digitalocean.com/community/tutorials/how-to-use-web-forms-in-a-flask-application

if __name__ == "__main__":
    app.run(debug=True)
