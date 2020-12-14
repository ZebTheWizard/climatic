from flask import render_template, session, request, jsonify
from app.models.Entry import Entry
import datetime
from dateutil import parser


def add():
    entry = Entry()
    now = datetime.datetime.now()
    created_at = request.json.get('datetime')
    if created_at:
        created_at = parser.parse(created_at)
    else:
        created_at = now
    entry = Entry.create_entry(created_at, request.json.get('humidity', 30), request.json.get('celsius', 14))

    return entry.insert()

def upload():
    rows = request.json.get("rows", [])
    now = datetime.datetime.now()
    for row in rows:
        created_at = parser.parse(row.get('created_at', now))
        humidity = row.get('humidity', 30)
        celsius = row.get('celsius', 14)
        entry = Entry.create_entry(created_at, humidity, celsius)
        entry.insert()
    return "success"

def remove():
    c = request.json.get('created_at')
    if c:
        created_at = parser.parse(c)
        entry = Entry()
        entry.query('WHERE created_at = ?', [created_at]).remove()
    return "success"

def list():
    entry = Entry()
    entries = entry.query("ORDER BY created_at DESC").get()
    return jsonify(entries[0]), entries[1]