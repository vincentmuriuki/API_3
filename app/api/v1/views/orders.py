# Python library imports
from flask import jsonify, request, make_response
from flask_restful import Resource

# Local imports
from ..models.orders import CustomerOrders

class Orders(Resource, CustomerOrders):
    """
    Orders
    """
    def __init__(self):
        self.man = CustomerOrders()
        

    def get(self):
        orders = self.man.retrieveorders()

        return make_response(jsonify(
            {
                'Message' : 'Order List',
                'Status' : 'Ok',
                'Orders' : orders
            }
        ))