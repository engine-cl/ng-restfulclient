#!/usr/bin/env python
__copyright__ = "Copyright (C) 2016 eNgine.cl"
__revision__ = "$Revision$"
__license__ = "BSD License"
__version__ = "$Version$"
__author__ = "Jorge A. Medina"
__date__ = "11/8/16"

from aiohttp import web

async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(body=text.encode('utf-8'))

app = web.Application()
app.router.add_route('GET', '/{name}', handle)

web.run_app(app)