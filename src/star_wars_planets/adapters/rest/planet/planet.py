from sanic_restful import Resource
from sanic.response import HTTPResponse, json

from star_wars_planets.application.planet.planet_application import PlanetApplication
from star_wars_planets.application.serializers import parse_request_body, parse_queries_string
from star_wars_planets.application.serializers.planet import PlanetSerializer


class PlanetsResource(Resource):

    planet_application: PlanetApplication = PlanetApplication()

    @parse_request_body(PlanetSerializer)    
    async def post(self, request, body: PlanetSerializer) -> HTTPResponse:
        return json(
            await self.planet_application.save_planet(body),
            status=201,
        )
    
    @parse_queries_string
    async def get(self, request, args: dict = None) -> HTTPResponse:
        return json(
            await self.planet_application.get_planets(args.get('name'))
        )
