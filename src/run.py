from sanic import Sanic
from sanic_motor import BaseModel

from config.default import Configuration
from star_wars_planets.adapters.rest import rest

app = Sanic(__name__)

app.blueprint(rest)
app.config.from_object(Configuration)
BaseModel.init_app(app)


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=6606,
        debug=app.config.APPLICATION_DEBUG,
        workers=app.config.APPLICATION_WORKERS_NUMBER,
    )
