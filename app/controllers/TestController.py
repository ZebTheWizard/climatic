from flask import render_template

# app = Flask('www')

# from src.www import app

# @app.route("/test")
def hello_world():
    return render_template("welcome.html")

# print("asdfasdfasdf", app.url_map)