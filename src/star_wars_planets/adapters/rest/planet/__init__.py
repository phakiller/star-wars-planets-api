from sanic_restful import Api
from sanic.blueprints import Blueprint

from . import planet


planet_bp = Blueprint(__name__, url_prefix='/planets')
planet_api = Api(planet_bp)

planet_api.add_resource(planet.PlanetsResource, '')
planet_api.add_resource(planet.PlanetResource, '/<planet_id:string>')
