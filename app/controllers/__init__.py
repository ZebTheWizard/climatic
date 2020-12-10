# from autoload import import_modules
# load_submodules(__name__)
# import_modules()

# from app.main import app
# from flask import Blueprint

# app.register_blueprint(Blueprint())

# import pkgutil
# import os

# # __all__ = []
# # for loader, module_name, is_pkg in pkgutil.walk_packages(__path__):
# #     __all__.append(module_name)
# #     _module = loader.find_module(module_name).load_module(module_name)
# #     globals()[module_name] = _module

# # print(__all__)


# directory = os.path.dirname(__file__)
# for loader, module_name, is_pkg in pkgutil.walk_packages(directory):
#     print(loader, module_name, is_pkg)

# print("hello world")
# print(os.path.dirname(__file__))
# print(pkgutil.walk_packages())

# print("hello __init__")
# from autoload import load_submodules
# print(load_submodules(__name__))