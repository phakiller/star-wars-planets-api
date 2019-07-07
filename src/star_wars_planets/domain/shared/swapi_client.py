from typing import List, Any
from dataclasses import field

from marshmallow_dataclass import dataclass

from . import ExternalClient


@dataclass
class SwapiPlanet:
    name: str
    films: List[str]


@dataclass
class SwapiPlanets:
    count: int = 0
    next: int = None
    previous: int = None
    results: List[SwapiPlanet] = field(
        default_factory=lambda: [],
    )


class SwapiClient(ExternalClient):
    BASE_URL = 'https://swapi.co/api'

    @classmethod
    async def get_planets(cls, **kwargs: Any) -> SwapiPlanets:
        planets = await cls._request(
            **kwargs,
            method='get',
            route='/planets',
        )
        return SwapiPlanets.Schema().load(planets).data if planets else None
    
    @classmethod
    async def find_planets_by_name(cls, name: str) -> SwapiPlanets:
        return await cls.get_planets(
            params={
                'search': name,
            }
        )
