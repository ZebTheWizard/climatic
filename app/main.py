from flask import Flask, send_from_directory, render_template
import os


static_folder = "../public"
error_pages = [404]
app = Flask(__name__,
    template_folder="../resources/views",
    static_folder=None, #static files are handled seperatly
    )



import routes.routes
from routes import _router, _print_routes

# for error in error_pages:
#     app.register_error_handler(error, (render_template("errors/" + str(error) + ".html"), error))
app.register_error_handler(404, lambda e: (render_template("/errors/" + str(404) + ".html"), 404))
app.register_blueprint(_router)


@app.route('/<path:path>')
def _serve_public_folder(path):
    print(path)
    return send_from_directory(static_folder, path)


if os.environ["FLASK_ENV"] == "development":
    _print_routes(app)




