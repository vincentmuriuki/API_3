# unittest
import unittest

# from run import app
from run import app
import json

from app import create_app

class TestOrders(unittest.TestCase):
    """
    This class contains tests for all the endpoints
    """
    def setUp(self):
        # app.testing = True
        self.app = create_app()
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()


    def test_get_orders(self):
        response = self.client.get(
            "/api/v1/orders",
            headers={"content-type": "application/json"}
        )
        
        self.assertEqual(response.status_code, 200)
    def tearDown(self):
        self.app_context.pop()
        