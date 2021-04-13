from src import api
from src.resources.aggregations import AggregationApi
from src.resources.films import FilmListApi
from src.resources.smoke import Smoke

api.add_resource(Smoke, '/smoke')
api.add_resource(FilmListApi, '/films', '/films/<uuid>', strict_slashes=False)
api.add_resource(AggregationApi, '/aggregations', strict_slashes=False)
