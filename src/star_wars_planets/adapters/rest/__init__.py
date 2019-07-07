from sanic import Blueprint

from .health import health_bp
from .planet import planet_bp


rest = Blueprint.group(
    health_bp,
    planet_bp
)
