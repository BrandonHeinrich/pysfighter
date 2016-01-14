import unittest
import pysfighter

class TestStocksOnVenue(unittest.TestCase):
    def setUp(self):
        self.stocks = pysfighter.core.stocks_on_venue("TESTEX")
    
    def tearDown(self):
        del self.stocks
    
    def test_stocks_is_list(self):
        self.assertEqual(type(self.stocks), list);
        
    def test_stocks_are_strings(self):
        for stock in self.stocks:
            self.assertEqual(type(stock), str)
    
    def test_stocks_on_testex(self):
        self.assertEqual(self.stocks[0], "FOOBAR")