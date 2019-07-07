from .planet import Planet
from ..shared.swapi_client import SwapiClient


class PlanetDomainApplication:
    async def save_planet(self, planet: Planet) -> None:
        await self.__set_number_of_movies_by_planet(planet)
        return await planet.save()
    
    async def __set_number_of_movies_by_planet(self, planet: Planet):
        response = await SwapiClient.find_planets_by_name(planet.name)

        if response:
            if response.count == 1 and response.results[0].name.lower() == planet.name.lower():
                planet.number_of_movies = len(response.results[0].films)
            else:
                planet.number_of_movies = 0
        else:
            planet.number_of_movies = -1
