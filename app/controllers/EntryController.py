from flask import render_template, session, request, jsonify
from app.models.Entry import Entry
import datetime
from dateutil import parser


def create_entry(created_at, humidity, celsius):
    entry = Entry()

    created_hour = created_at.strftime("%Y-%m-%d %H:00:00")
    created_day = created_at.strftime("%Y-%m-%d 00:00:00")
    created_month = created_at.strftime("%Y-%m-01 00:00:00")
    created_year = created_at.strftime("%Y-01-01 00:00:00")

    entry.created_at = created_at
    entry.create_hour = created_hour
    entry.create_day = created_day
    entry.create_month = created_month
    entry.create_year = created_year
    entry.humidity = float(humidity)
    entry.celsius = float(celsius)

    return entry

def add():
    entry = Entry()
    now = datetime.datetime.now()
    mstr = request.json.get('datetime', now.strftime("%Y-%m-%d %H:%M:%S"))
    created_at = datetime.datetime.strptime(datestr, "%Y-%m-%d %H:%M:%S")
    entry = create_entry(create_entry, request.json.get('humidity', 30), request.json.get('celsius', 14))

    return entry.insert()

def upload():
    rows = request.json.get("rows", [])
    now = datetime.datetime.now()
    for row in rows:
        created_at = parser.parse(row.get('created_at', now))
        humidity = row.get('humidity', 30)
        celsius = row.get('celsius', 14)
        entry = create_entry(created_at, humidity, celsius)
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