from dataclasses import field

from marshmallow_dataclass import dataclass


@dataclass
class PlanetSerializer:
    id: str = field(
        default=None,
        metadata={'attribute': '_id', 'dump_only': True,}
    )
    name: str = field(
        default=None,
        metadata={'required': True,}
    )
    climate: str = field(
        default=None,
        metadata={'required': True,}
    )
    terrain: str = field(
        default=None,
        metadata={'required': True,}
    )
    number_of_movies: int = field(
        default=None,
        metadata={'dump_only': True,}
    )
