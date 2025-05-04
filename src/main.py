from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from . import search_places

app = FastAPI()

app.mount('/static',StaticFiles(directory='static'))
app.include_router(search_places.router)



