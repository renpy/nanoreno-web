import flask
import functools

# The flask application.
app = flask.Flask(__name__)

class Error(Exception):
    """
    Indicates that a web request had an error. This may be raised
    or returned from an api function.
    """

    def __init__(self, message):
        self.message = message

def api(f, key=""):

    @functools.wraps(f)
    def wrapper(*args, **kwargs):

        rv = { }

        try:
            result = f(*args, **kwargs)
            if result is not None:
                rv = result

        except Error as e:
            rv["error"] = e.message

        return flask.jsonify(**rv)

    api_path = "/api/" + wrapper.__name__ + key
    app.add_url_rule(api_path, wrapper.__name__, wrapper, methods=[ 'GET', 'POST' ])

    return f

def api_key(f):
    return api(f, "/<key>")

@api
def test_api():
    return True

# @app.route("/api/<path:path>")
# def bad_api(path):
#     return flask.jsonify({ "error" : "{} is not an api endpoint." })

