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
