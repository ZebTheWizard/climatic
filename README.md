# Climatic Group Project Scaffold

This branch only contains the scaffold for the flask application. To see a working site, visit the master branch.

### Minimal Installation/Run

##### Linux/Mac
1. Create the virtual environment `python -m venv venv`
1. Activate the environment `source venv/bin/active`
1. Install pip requirements `pip install -r requirements.txt`
1. Run the server `./run.sh`

##### Windows (Git bash / WSL)
1. Create the virtual environment `python -m venv venv`
1. Activate the environment `source venv/Scripts/active`
1. Install pip requirements `pip install -r requirements.txt`
1. Run the server `./run.sh`

##### Windows (CMD / PowerShell)
1. Create the virtual environment `python -m venv venv`
1. Activate the environment `venv/Scripts/active.bat`
1. Install pip requirements `pip install -r requirements.txt`
1. Run the server `run.bat`


### File structure
The file structure was created for easy file seperation. Routing, logic, and views are all seperate. The server also autoloads logic and binds it to the appropriate routes. This means you don't have to mess with main.py.

- **app/** - the logic to the application. 
- **app/controllers/** - Files in this directory are automatically imported when the server restarts.
- **public/** - Static assets and bundled js/css files. Everything in the public folder is available through the `/<path>` route. 
- **resources/views** - All the jinja views for the project including layouts. By default, the project uses **Bootstrap 5**
- **resources/views/errors** - This folder contains views for custom error messages. To create a view for an error code use this naming scheme. `<error>.html`. 
- **resources/assets** - Unbundled assets. Use preprocessors and npm packages for front-end code. Bundle the code for browsers by running `yarn build` or `npm run build`
- **routes/routes.py** - the routing config for the entire project. no logic. just routes.


### Understanding Routes
Flask caches routes when the server restarts. This means autoloading does not affect the performance of the web server. 

Since autoloading is used. Business logic from the app/controllers directory does not need to be reimported. It can be referenced using a 'magic' string like `TestController@hello_world`. The router will automatically figureout which method to bind to the route.

##### Why file seperation
When flask apps get bigger than a few pages, python files start to get very large which makes it difficult to read and debug. This leads to file seperation, but file seperation makes it difficult to debug route matching priorty. 

By seperating the routes from the business logic entirely, it is clear which routes are available and when they are matched. 


##### Writing routes
routes can be called a few ways. The most versitile way is the following. `route(<method_list>, <path>, <function_pointer>)`

```
import app.controllers.TestController

route(["PUT"], "/my/route", TestController.hello_world)
```

However, most routes use GET or POST. So a step can be saved.
```
import app.controllers.TestController

route_get("/my/route", TestController.hello_world)
```

But there is no need to import code in the app/controllers directory because that code is already autoloaded. So, you can use a 'magic' string. No import needed.
```
route_get("/my/route", "TestController@hello_world")
```


### Understanding resources
A lot of existing code for JS/CSS is available through NPM. Code can be downloaded and modified by using `yarn` or `npm` build tools. However, the code will not run in older browsers by default. The solution is bundling.

Bundling not only makes the packages available in the browser, it can also improve the code for production environments. Bundling can automatically minify, shakeout unused code, or add browser support through polyfills and autoprefixing. 

By default, this project uses **parcel2** but other alternatives such as **webpack**, **rollup**, **snowpack**, or **gulp** can be used.

##### I want to change CSS/JS
All you do is modify the code in `resources/assets` folder. Then run `yarn build` or `npm run build`. You must have yarn or npm installed for this to work.

##### Where are the views?
The views are stored in the `resources/views` directory.

