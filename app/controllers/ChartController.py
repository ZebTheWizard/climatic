from flask import render_template, session, request, jsonify
from app.models.Entry import Entry
from datetime import datetime, timedelta

def shape_entries(entries, date_column):
    data = {
        'times': [],
        'temps': [],
        'humid': []
    }
    for e in entries[0]:
        data['times'].append(e.get(date_column))
        data['temps'].append(e.get('celsius') / e.get('count'))
        data['humid'].append(e.get('humidity') / e.get('count'))
    
    return data

def fetch_entries(cutoff, date_column):
    entry = Entry()
    entries = entry.query("where created_at >= ? GROUP BY %s ORDER BY created_at ASC" % date_column, [cutoff]) \
        .get("count(*) as count, sum(humidity) as humidity, sum(celsius) as celsius, %s" % date_column)

    return jsonify(shape_entries(entries, date_column)), entries[1]

def default():
    cutoff = datetime.now() - timedelta(hours=1)
    return fetch_entries(cutoff, 'create_5minute')

def last6hours():
    cutoff = datetime.now() - timedelta(hours=6)
    return fetch_entries(cutoff, 'create_hour')

def last24hours():
    cutoff = datetime.now() - timedelta(hours=24)
    return fetch_entries(cutoff, 'create_hour')

def last7days():
    cutoff = datetime.now() - timedelta(days=7)
    return fetch_entries(cutoff, 'create_day')

def last30days():
    cutoff = datetime.now() - timedelta(days=30)
    return fetch_entries(cutoff, 'create_day')

def last180days():
    cutoff = datetime.now() - timedelta(days=180)
    return fetch_entries(cutoff, 'create_month')

def last365days():
    cutoff = datetime.now() - timedelta(days=365)
    return fetch_entries(cutoff, 'create_month')

def all():
    date_column = "create_year"
    entry = Entry()
    entries = entry.query("GROUP BY %s ORDER BY created_at ASC" % date_column) \
        .get("count(*) as count, sum(humidity) as humidity, sum(celsius) as celsius, %s" % date_column)
    return  jsonify(shape_entries(entries, date_column)), entries[1]