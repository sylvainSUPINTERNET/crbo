from aiohttp import web

from middlewares.example import handle

def getRoutes():
    return [
            web.get('/', handle),
            web.get('/{name}', handle)]

