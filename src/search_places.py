import requests
from os import getenv
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from .templates import templates
from .utils import generate_params, get_places

router = APIRouter()

search_url = getenv('foursquare_search_url')

headers = {
    "Accept": "application/json",
    "Authorization": getenv('foursquare_api_key')
}


@router.get("/")
def index(request: Request) -> HTMLResponse:
    """
    Главная страница

    :param request: Объект Request
    :return: Объект HTMLResponse
    """
    return templates.TemplateResponse(request=request, name='index.html')


@router.get('/places-list')
def places_list(request: Request) -> HTMLResponse:
    """
    Страница поиска мест

    :param request: объект Request
    :return: объект HTMLResponse
    """
    query_params = dict(request.query_params)
    params = generate_params(query_params)
    if not params:
        places = []
    else:
        response = requests.get(url=search_url,params=params,headers=headers)
        data = response.json()
        places = get_places(data,query_params)
    return templates.TemplateResponse(request=request,name='places_list.html',context={'places':places})

