import pandas
from app.helpers import has_allowed_ext, save_file, error_json
from flask import request, redirect, flash, jsonify, current_app

def upload_csv():
    input_name = 'csv_file'
    schema = ["date", "time", "temp_c", "humidity"]

    if input_name in request.files:
        file = request.files[input_name]
        if file and has_allowed_ext(file.filename, ['csv']):
            location = save_file(current_app.storage_path, 'csv_files', file=file)
            data = pandas.read_csv(location)
            if set(schema).issubset(data.to_dict().keys()):
                return jsonify(data.to_json(orient='records'))
            else:
                return error_json("CSV must have [%s] columns" % ", ".join(shema))
        else:
            return error_json("File must be CSV file")
    else:
        return error_json("Could not upload or parse file")
    return error_json("unexpected error")