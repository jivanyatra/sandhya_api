from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route

async def homepage(request):
    return JSONResponse({'hello': 'world'})

async def sandhya(request):
    return JSONResponse({'method': request.method,
                         'url': request.url,
                         })

async def get_times(lat, long, date):
    pass


app = Starlette(debug=True, routes=[
    Route('/', homepage),
])