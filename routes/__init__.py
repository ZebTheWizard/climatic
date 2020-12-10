from flask import Blueprint
from autoload import load_submodules
import app.controllers

_router = Blueprint('router', __name__)
_controllers = load_submodules(app.controllers)
def route(methods, url, func):
    global _router
    global _controllers
    if isinstance(func, str):
        module_name, method_name = func.split("@")
        module = _controllers.get("app.controllers." + module_name)
        method = getattr(module, method_name)
        _router.add_url_rule(url, view_func=method, methods=methods)
    else:
        _router.add_url_rule(url, view_func=func, methods=methods)

def route_get(url, func):
    route(["GET"], url, func)

def route_post(url, func):
    route(["POST"], url, func)

