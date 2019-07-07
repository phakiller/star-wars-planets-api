from sanic import Blueprint

from .health import health_bp


rest = Blueprint.group(
    health_bp
)
