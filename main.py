import os
import func
import json
from flask import Flask, render_template, request, url_for
import numpy as np
from platform import system as running_os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24).hex()

with open("config.json", "r") as file:
    config = json.load(file)

calculation = []
mode_calculation = "numerical culation"

def shutdown():
    print("shutting down")
    if running_os() == "Linux":
        print("killing node")
        os.system("killall node & kill $(pgrep electron)")
    if running_os() == "Windows":
        os.system("taskkill /IM node.exe /F")
    quit()

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
        return(render_template("programmation.html", config=config))
    if value == "shutdown":
        shutdown()
    if value == "settings":
        return(render_template("settings.html", config=config))
    if value == "menu":
        return(render_template("main.html", config=config))
    else:
        return(render_template("main.html", config=config))

@app.route("/submit", methods=["GET", "POST"])
def submit():
    valueMenu = request.form.get('menu', None)
    valueText = request.form.get('text', None)
    if valueMenu:
        if valueMenu == "menu":
            return(render_template("main.html", config=config))
        if valueMenu == "settings":
            return(render_template("settings.html", config=config))

    result, resultType = func.calculate(valueText)
    result = str(result)

    if resultType == "clear":
        calculation.clear()
        
    else:
        try:
            func.ans = float(result)
            func.history.append((valueText,float(result)))
        except:
            print("ans not supported")
        print(calculation)
        calculation.insert(0, {
            "calculation": (valueText, result),
            "type": resultType,
            "graphNumber": str(len(os.listdir("static/graphs"))) if resultType == "graph" else None
        })
    return(render_template("calculation.html", calculation=calculation, config=config))

if __name__ == "__main__":
    app.run(debug=True)
