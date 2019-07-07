from functools import wraps

from sanic.response import json
from marshmallow import ValidationError


def parse_request_body(serializer):
    def decorator(func):
        @wraps(func)
        async def decorated_function(_self, request, *args, **kwargs):
            try:
                kwargs['body'] = serializer.Schema(strict=True).load(request.json or {}).data
            except ValidationError as err:
                return json(body=err.messages, status=400)
            
            return await func(_self, request, *args, **kwargs)
        return decorated_function
    return decorator


def parse_queries_string(func):
    @wraps(func)
    async def decorated_function(_self, request, *args, **kwargs):
        kwargs['args'] = dict(request.query_args)
        return await func(_self, request, *args, **kwargs)
    return decorated_function
