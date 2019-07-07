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
