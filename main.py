from flask import Flask, render_template, request, send_from_directory, current_app
import os
from concurrent.futures import ProcessPoolExecutor

app = Flask(__name__)

@app.route("/")
def home():
    return(render_template("calculation.html"))

@app.route('/submit', methods=['POST'])
def submit():
    value = request.form['text']
    print(value)
    return value

if __name__ == "__main__":
    app.run(debug=True)
