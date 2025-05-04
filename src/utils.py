category_ids = {
    'food_filter': 13000,
    'entertainments_filter':10000,
    'purchases_filter': 17000,
}


def get_categories(query: dict) -> str:
    """Обработка категорий"""
    filters = []

    for i in query:
        category_num = category_ids.get(i, "")
        if category_num:
            filters.append(str(category_num))

    return ",".join(filters)


def generate_params(query: dict) -> dict:
    """Создание параметров для запроса к foursquare api"""
    needed_params = ('query','near')
    params = {}

    categories = get_categories(query)

    if categories:
        params['categories'] = categories

    for i in query:
        if query[i] and i in needed_params:
            params[i] = query[i]

    if not params:
        return params
    else:
        params.update({'limit': 30, 'fields': 'name,rating,website,location'})
    return params


def rating_filter(data: dict,query: dict) -> list:
    """Фильтрация по рейтингу"""
    places = []

    rating_from = query.get('rating_from')
    rating_to = query.get('rating_to')

    if not rating_from:
        rating_from = float(0)
    else:
        rating_from = float(rating_from)

    if not rating_to:
        rating_to = float(10)
    else:
        rating_to = float(rating_to)

    for i in data.get('results',[]):
        if i.get('rating',0):
            if rating_from <= i['rating'] <= rating_to:
                places.append(i)
        else:
            places.append(i)
    return places


def get_places(data: dict,query: dict) -> list:
    """Дополнительная обработка полученных результатов, применение фильтров и т.д."""
    data = rating_filter(data,query)
    return data
