import time
import threading
import app.main as Service
import logging

from flask import request
from werkzeug.serving import make_server



class ServerThread(threading.Thread):

    def __init__(self, app):
        threading.Thread.__init__(self)
        app.logger.disabled = True
        self.server = make_server('0.0.0.0', 80, app)
        self.ctx = app.app_context()
        self.ctx.push()

    def run(self):
        print("Web server running on http://0.0.0.0:80")
        self.server.serve_forever()

    def shutdown(self):
        self.server.shutdown()

server = ServerThread(Service.app)

def make(schedule):
    global server
    server.start()
    log = logging.getLogger('werkzeug')
    log.disabled = True


def destroy():
    global server
    server.shutdown()