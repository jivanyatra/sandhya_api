import contextlib
import httpx
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route


async def homepage(request):
    return JSONResponse({'hello': 'world'})


@contextlib.asynccontextmanager
async def lifespan(app):
    async with httpx.AsyncClient() as client:
        yield {"http_client": client}


async def sandhya(request):
    client = request.state.http_client

    response = await get_times(client, request)
    return JSONResponse({'method': request.method,
                         'url': request.url,
                         })


async def get_times(http_client, lat, lng, date):
    """
    Uses sunrise-sunset.org's api to get the solar event times in UTC
    :param http_client: http client for the get request
    :param lat: latitude as float
    :param lng: longitude as float
    :param date: as string, '2023-01-29'
    :return: json
    """
    base_url = 'https://api.sunrise-sunset.org/json'
    params = {
        'lat': lat,
        'lng': lng,
        'date': date,
    }
    response = await http_client.get(base_url, params=params)
    return response.json()


app = Starlette(debug=True,
                routes=[
    Route('/', homepage),
    Route('/sandhya', sandhya),
],
                lifespan=lifespan,
                )