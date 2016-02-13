from flask import request
import flask
from werkzeug.exceptions import NotFound

import os

flask_yeoman = flask.Blueprint('flask_yeoman', __name__)

YEOMAN_DEBUG = int(os.environ.get('FLASK_YEOMAN_DEBUG', False))
ROOT = os.path.dirname(__file__)

if YEOMAN_DEBUG:
    SEARCH = [
        os.path.join(ROOT, "app"),
        os.path.join(ROOT, ".tmp"),
        ROOT
        ]

else:
    SEARCH = [
        os.path.join(ROOT, "dist")
        ]

@flask_yeoman.route('/bower_components/<path:path>')
@flask_yeoman.route('/styles/<path:path>')
@flask_yeoman.route('/scripts/<path:path>')
@flask_yeoman.route('/views/<path:path>')
@flask_yeoman.route('/images/<path:path>')
def serve_resource(path):
    path = request.path[1:]

    for p in SEARCH:
        fn = flask.safe_join(p, path)
        if os.path.exists(fn):
            return flask.send_file(fn)

    raise NotFound()


@flask_yeoman.route('/')
@flask_yeoman.route('/<path:path>')
def serve_index(path=None):

    for p in SEARCH:
        fn = flask.safe_join(p, "index.html")
        if os.path.exists(fn):
            break
    else:
        raise NotFound()

    return flask.send_file(fn)
