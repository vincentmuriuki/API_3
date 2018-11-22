# Python library imports
from flask_restful import Api
from flask import Blueprint
# LOcal imports
from .views.orders import Orders, NewOrder

apiV1 = Blueprint('api1', __name__, url_prefix='/api/v1')


api = Api(apiV1)

api.add_resource(Orders, '/orders')

api.add_resource(NewOrder, '/orders/new')