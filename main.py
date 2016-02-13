from flask_yeoman import flask_yeoman
from flask_failsafe import failsafe

@failsafe
def create_app():
    from web.app import app
    app.register_blueprint(flask_yeoman)

    return app

if __name__ == "__main__":
    create_app().run(port=5005, debug=True)
