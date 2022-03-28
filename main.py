import os
import func
from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24).hex()

calculation = []

@app.route("/")
def home():
    return(render_template("main.html", calculation=[]))

@app.route("/", methods=["GET", "POST"])
def redirectCalc():
    value = request.form["menu"]
    if value == "calc":
        return(render_template("calculation.html"))
    if value == "function":
        return(render_template("main.html"))
    if value == "program":
        return(render_template("main.html"))
    else:
        return(render_template("main.html"))


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
    return(render_template("calculation.html", calculation=calculation))

# https://towardsdatascience.com/using-python-flask-and-ajax-to-pass-information-between-the-client-and-server-90670c64d688
# https://www.digitalocean.com/community/tutorials/how-to-use-web-forms-in-a-flask-application

if __name__ == "__main__":
    app.run(debug=True)
