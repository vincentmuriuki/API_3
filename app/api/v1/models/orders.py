
from flask import jsonify
orders = []


class CustomerOrders():


    def __init__(self):
        self.orders = orders

    def save(self, name, price, quantity):
        order_accompanment = {
            'order_id': len(orders) + 1,
            'Description': {'Name of Snack' : name},
            'Price': price,
            'Quantity': quantity
        }
        
        self.orders.append(order_accompanment)

        return self.orders

    def retrieveorders(self):
        return self.orders
        