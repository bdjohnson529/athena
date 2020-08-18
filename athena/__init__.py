import os
from flask import Flask, render_template





def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = 'dev',
        DATABASE = os.path.join(app.instance_path, 'athena.sqlite'),
        UPLOAD_FOLDER = './uploads',
    )
    
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    from . import db
    db.init_app(app)


    from . import home
    app.register_blueprint(home.bp)
    app.add_url_rule('/', endpoint='index')


    from . import library
    app.register_blueprint(library.bp)


    return app