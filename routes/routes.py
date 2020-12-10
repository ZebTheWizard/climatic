from . import route_get
from app.controllers import TestController

route_get('/test2', TestController.hello_world)
route_get('/test', TestController.hello_world)
