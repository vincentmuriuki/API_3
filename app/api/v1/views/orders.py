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

class NewOrder(Resource, CustomerOrders):
    def __init__(self):
        self.man = CustomerOrders()

    def post(self):
        data = request.get_json()
        name = data['name']
        price = data['price']
        quantity = data['quantity']

        res = self.man.save(name, price, quantity)
        return make_response(jsonify(
            {
                'Status' : 'Delivered',
                'Message' : 'Order Placed!',
                'Order_Data' : res
            }
        ))