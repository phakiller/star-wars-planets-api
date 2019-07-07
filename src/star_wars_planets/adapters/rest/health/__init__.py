from sanic_restful import Api
from sanic.blueprints import Blueprint

from . import healthcheck


health_bp = Blueprint(__name__, url_prefix='/health')
health_api = Api(health_bp)

health_api.add_resource(healthcheck.HealthStatusResource, '/status')
