import importlib
import pkgutil
import sys

def load_submodules(package, recursive=True):
    if isinstance(package, str):
        package = importlib.import_module(package)
    results = {}
    for loader, name, is_pkg in pkgutil.walk_packages(package.__path__):
        full_name = package.__name__ + '.' + name
        results[full_name] = importlib.import_module(full_name)
        if recursive and is_pkg:
            results.update(load_submodules(full_name))
    return results


def import_modules(module):
    for loader, module_name, is_pkg in pkgutil.walk_packages(module.__path__, module.__name__ + '.'):
        importlib.import_module(module_name)