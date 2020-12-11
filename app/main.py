from flask import Flask, send_from_directory, render_template
from app.models import run_migrations_up, run_migrations_down
import os


static_folder = "../public"
error_pages = [404]
app = Flask(__name__,
    template_folder="../resources/views",
    static_folder=None, #static files are handled seperatly
    )

app.secret_key = "thisshouldbestorednothardcoded"
app.storage_path = os.path.join(os.path.realpath(__file__), '..', 'storage')


import routes.routes
from routes import _router, _print_routes

for error in error_pages:
    app.register_error_handler(error, lambda e: (render_template("/errors/" + str(error) + ".html"), error))
app.register_blueprint(_router)



@app.route('/<path:path>')
def _serve_public_folder(path):
    print(path)
    return send_from_directory(static_folder, path)


if os.environ["FLASK_ENV"] == "development":
    _print_routes(app)
    # run_migrations_down()
    
run_migrations_up()




