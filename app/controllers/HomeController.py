from flask import render_template, session, request
from app.models.Entry import Entry

def theme():
    mode = request.json.get('mode', 'light')
    if mode != "light":
        mode = "dark"
    session['theme'] = mode
    return mode

def welcome():
    return render_template("welcome.html")

