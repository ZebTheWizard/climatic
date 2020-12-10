from . import route_get, route_post, route
from app.controllers import TestController


route_get('/', TestController.hello_world)

route_get('/test', "TestController@hello_world")

route(["GET"], "/test2", "TestController@hello_world")
route(["GET"], "/test3", "TestController@hello_world")
