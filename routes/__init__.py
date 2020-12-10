from flask import Blueprint
from autoload import load_submodules
import app.controllers
import urllib
import inspect
import time

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

def _print_routes(_app):
    time.sleep(0.5)
    fmt = "{:<10} {:40s} {:30s} {:50s}"
    print()
    print("=== LOADED ROUTES ====")
    print(fmt.format("priorty","route","methods","location"))
    locations = {}
    for name, func in _app.view_functions.items():
        # print(name, func)
        path = inspect.getfile(func)
        line = inspect.getsourcelines(func)[1]
        locations[name] = path + ":" + str(line)

    arr = []
    for i in range(len(_app.url_map._rules)):
        rule = _app.url_map._rules[i]
        loc = locations.get(rule.endpoint)
        methods = ",".join(rule.methods)
        line = urllib.parse.unquote(fmt.format(i, str(rule), methods, loc))
        arr.append(line)
    
    for line in arr:
        print(line)

    print()
    print()