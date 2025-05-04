import requests
from os import getenv
from fastapi import APIRouter
from fastapi import Request
from .templates import templates
from .utils import generate_params, get_places

router = APIRouter()

url = "https://api.foursquare.com/v3/places/search"

headers = {
    "Accept": "application/json",
    "Authorization": getenv('foursquare_api_key')
}


@router.get("/")
def index(request: Request):
    """Главная страница"""
    return templates.TemplateResponse(request=request, name='index.html')


@router.get('/places-list')
def places_list(request: Request):
    """Страница поиска мест"""
    query_params = dict(request.query_params)
    params = generate_params(query_params)
    if not params:
        places = []
    else:
        response = requests.get(url=url,params=params,headers=headers)
        data = response.json()
        places = get_places(data,query_params)
    return templates.TemplateResponse(request=request,name='places_list.html',context={'places':places})
