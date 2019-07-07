from sanic_restful import Resource
from sanic.response import HTTPResponse, json

from star_wars_planets.application.planet.planet_application import PlanetApplication
from star_wars_planets.application.serializers import parse_request_body
from star_wars_planets.application.serializers.planet import PlanetSerializer


class PlanetsResource(Resource):

    planet_application: PlanetApplication = PlanetApplication()

    @parse_request_body(PlanetSerializer)    
    async def post(self, request, body: PlanetSerializer) -> HTTPResponse:
        return json(
            await self.planet_application.save_planet(body),
            status=201,
        )
    
    async def get(self, request) -> HTTPResponse:
        return json(
            await self.planet_application.get_planets()
        )
