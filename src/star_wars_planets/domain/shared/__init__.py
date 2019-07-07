import aiohttp

from sanic.log import logger
from aiohttp.client_exceptions import ClientConnectorError


class ExternalClient:
    BASE_URL = None
    
    @classmethod
    async def _request(cls, method: str, route: str, params: dict = None, json: dict = None) -> dict:
        async with aiohttp.ClientSession() as session:
            try:
                async with session.request(
                    url=f'{cls.BASE_URL}{route}',
                    method=method,
                    params=params,
                    json=json,
                ) as resp:
                    return await resp.json()
            except ClientConnectorError:
                logger.error(f'ConnectionError: {cls.BASE_URL}{route}')
                return None
