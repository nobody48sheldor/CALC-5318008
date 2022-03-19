from flask import Flask, render_template, request, send_from_directory, current_app
import os
from concurrent.futures import ProcessPoolExecutor

app = Flask(__name__)

@app.route("/")
def home():
    return(render_template("main.html"))

def main():
    with ProcessPoolExecutor() as executor:
        f1 = executor.submit(run)
        f2 = executor.submit(os.system, "npm start")

def run():
    if __name__ == "__main__":
        app.run(debug=True)

if __name__ == "__main__":
    main()
