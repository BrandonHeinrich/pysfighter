import unittest
import pysfighter

class TestOrderbook(unittest.TestCase):
    def setUp(self):
        self.orderbook = pysfighter.core.orderbook()
    
    def tearDown(self):
        del self.orderbook
        
    def test_orderbook_timestamp(self):
        self.assertEqual(type(self.orderbook.timestamp), int)