from __future__ import annotations

from sanic_motor import BaseModel


class Planet(BaseModel):
    __coll__ = 'planets'
    __unique_fields__ = ['_id',]

    _id: str
    name: str
    climate: str
    terrain: str
    number_of_movies: int

    def to_dict(self):
        return {
            'name': self.name,
            'climate': self.climate,
            'terrain': self.terrain,
            'number_of_movies': self.number_of_movies,
        }

    async def save(self) -> Planet:
        res = await self.insert_one(self.to_dict())
        self._id = res.inserted_id
        return self
    
    @classmethod
    async def get_planets(cls):
        return await cls.find()
    
    @classmethod
    async def find_planets_by_name(cls, name: str):
        return await cls.find(
            None,
            {
                'name': {
                    '$regex': name,
                    '$options': 'ix'
                }
            }
        )
    
    @classmethod
    async def find_planet_by_id(cls, id):
        return await cls.find_one(id)
    
    @classmethod
    async def delete_planet_by_id(cls, _id: str):
        return await cls.find_one_and_delete(
            {
                '_id': cls.get_oid(_id)
            }
        )
