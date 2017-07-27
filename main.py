from flask import Flask
from config import Config


def make_app(config):
    """ Returns a Flask object ready to serve the website. """

    # Create a Flask app object.
    app = Flask(__name__)
    app.config.from_object(config)

    # Register endpoints.
    import views
    app.register_blueprint(views.base.blueprint)

    return app


if __name__ == "__main__":
    config = Config()
    app = make_app(config)
    app.run(port=config.port)
