import aiohttp
import asyncio

loop = asyncio.get_event_loop()

async def _call(http_method=None, url=None, *args, **kwargs):
    session = aiohttp.ClientSession()
    async with eval('session.' + http_method)(url) as response:
        assert response.status == 200
        return await response.text()


def _serializer(*args, **kwargs):
    if len(args) and len(kwargs):
        return args, kwargs
    elif len(args):
        return args
    else:
        return kwargs

async def head(url=None, serializer=_serializer, *args, **kwargs):
    """
    get method implementation
    :param url:
    :param serializer: callback function
    :param args:
    :param kwargs:
    :return:
    """
    return serializer(await _call(http_method='head', url=url))

async def get(url=None, serializer=_serializer, *args, **kwargs):
    """
    get method implementation
    :param url:
    :param serializer: callback function
    :param args:
    :param kwargs:
    :return:
    """
    return serializer(await _call(http_method='get', url=url))


async def post(url=None, serializer=_serializer, *args, **kwargs):
    """
    put method implementation
    :param url:
    :param serializer: callback function
    :param args:
    :param kwargs:
    :return:
    """
    if len(args):
        kwargs['payload'] = args[0]
    return serializer(await _call(http_method='post', url=url, data=kwargs['payload']))


async def options(url=None, serializer=_serializer, *args, **kwargs):
    """
    option method implementation
    :param url:
    :param serializer: callback function
    :param args:
    :param kwargs:
    :return:
    """
    return serializer(await _call(http_method='options', url=url))


async def delete(url=None, serializer=_serializer, *args, **kwargs):
    """
    delete method implementation
    :param url:
    :param serializer: callback function
    :param args:
    :param kwargs:
    :return:
    """
    return serializer(await _call(http_method='delete', url=url))


def event_loop(callback=None):
    loop.run_until_complete(callback())
