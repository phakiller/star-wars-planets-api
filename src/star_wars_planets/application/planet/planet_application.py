from star_wars_planets.domain.planet.planet_domain_application import PlanetDomainApplication
from star_wars_planets.domain.planet.planet import Planet
from ..serializers.planet import PlanetSerializer


class PlanetApplication:

    planet_domain_application = PlanetDomainApplication()

    async def save_planet(self, planet_command: PlanetSerializer) -> dict:
        planet = Planet(
            name=planet_command.name,
            climate=planet_command.climate,
            terrain=planet_command.terrain,
        )
        await self.planet_domain_application.save_planet(planet)
        return PlanetSerializer.Schema().dump(planet).data
    
    async def get_planets(self, name: str = None) -> dict:
        if name:
            planets = await Planet.find_planets_by_name(name)
        else:
            planets = await Planet.get_planets()
        return PlanetSerializer.Schema().dump(planets.objects, many=True).data
    
    async def find_planet_by_id(self, id: str):
        planet = await Planet.find_planet_by_id(id)
        if planet:
            return PlanetSerializer.Schema().dump(planet).data
    
    async def delete_planet_by_id(self, id: str):
        planet = await Planet.delete_planet_by_id(id)
        if planet:
            return PlanetSerializer.Schema().dump(planet).data
