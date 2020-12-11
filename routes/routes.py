from . import route_get, route_post, route


route_get('/', "HomeController@welcome")
route_post('/theme', "HomeController@theme")

route_post('/entry/add', "EntryController@add")
route_get('/entry/list', "EntryController@list")
route_post('/entry/upload', "EntryController@upload")
route_post('/entry/remove', "EntryController@remove")

route_get('/entry/list/default', "ChartController@default")
route_get('/entry/list/last24hours', "ChartController@last24hours")
route_get('/entry/list/last7days', "ChartController@last7days")
route_get('/entry/list/last30days', "ChartController@last30days")
route_get('/entry/list/last180days', "ChartController@last180days")
route_get('/entry/list/last365days', "ChartController@last365days")
route_get('/entry/list/all', "ChartController@all")