from sanic_restful import Resource
from sanic.response import json


class HealthStatusResource(Resource):
    async def get(self, request):
        return json({'status': 'OK'})
