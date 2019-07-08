from sanic import Sanic
from sanic_motor import BaseModel
from sanic_cors import CORS

from config.default import Configuration
from star_wars_planets.adapters.rest import rest


def create_app(configuration=Configuration):
    app = Sanic(__name__)
    CORS(app)

    app.blueprint(rest)
    app.config.from_object(configuration)
    BaseModel.init_app(app)

    return app
