from aiohttp import web

async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    data = { "name" :"toto"}
    return web.json_response(data)