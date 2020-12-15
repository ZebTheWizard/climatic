import os
from werkzeug.utils import secure_filename
from flask import jsonify
from datetime import datetime, timedelta

def has_allowed_ext(filename, extensions):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in extensions

def create_directory(*args, **kwargs):
    if 'file' in kwargs:
        return os.path.join(create_directory(*args), kwargs.get('file'))

    loc = os.path.join(*args)
    
    if not os.path.exists(loc):
        os.makedirs(loc)
    return loc

def hash_filename(filename):
    _, ext = secure_filename(filename).rsplit('.', 1)
    now = int(round(time.time() * 1000))
    seed = str(now) + filename
    return str(hash(seed)) + "." + ext

def save_file(*args, **kwargs):
    file = kwargs.get('file')
    filename = hash_filename(file.filename)
    location = create_directory(*args, file=filename)
    file.save(location)
    return location

def error_json(msg):
    return jsonify({"error": msg}), 500


def ceil_date(date, **kwargs):
    seconds = timedelta(**kwargs).total_seconds()
    return datetime.fromtimestamp(date.timestamp() + seconds - date.timestamp() % seconds)

def floor_date(date, **kwargs):
    seconds = timedelta(**kwargs).total_seconds()
    return datetime.fromtimestamp(date.timestamp() - date.timestamp() % seconds)