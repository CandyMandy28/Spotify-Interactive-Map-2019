from flask import Flask
from flask import request

app = Flask(__name__)

# Command to run
# FLASK_APP=hello.py flask run

@app.route('/')
def welcome():
    return "Welcome to Spotify Interactive Map!\nPlease type in an Artist that you would like to see!"

@app.route('/<artist_id>')
def artist(artist_id):
    #start the map
    pass

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # do login
        pass
    else:
        # show login form
        pass

# import os

# from flask import Flask

# def create_app(test_config=None):
#     # create and configure the app
#     app = Flask(__name__, instance_relative_config=True)
#     app.config.from_mapping(
#         SECRET_KEY='dev',
#         DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
#     )

#     if test_config is None:
#         # load the instance config, if it exists, when not testing
#         app.config.from_pyfile('config.py', silent=True)
#     else:
#         # load the test config if passed in
#         app.config.from_mapping(test_config)

#     # ensure the instance folder exists
#     try:
#         os.makedirs(app.instance_path)
#     except OSError:
#         pass

#     # a simple page that says hello
#     @app.route('/')
#     def welcome():
#         return "Welcome to Spotify Interactive Map!\nPlease type in an Artist that you would like to see!"

#     return app