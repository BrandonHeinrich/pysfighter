import unittest
import pysfighter

class TestHeartbeat(unittest.TestCase):
    def setUp(self):
        self.heartbeat = pysfighter.core.heartbeat()
    
    def tearDown(self):
        del self.heartbeat
    
    def test_heartbeat_has_ok(self):
        self.assertIn("ok", self.heartbeat)
        
    def test_heartbeat_has_error(self):
        self.assertIn("error", self.heartbeat)
        
    def test_heartbeat_ok_is_bool(self):
        self.assertEqual(type(self.heartbeat["ok"]), bool);
        
    def test_heartbeat_error_is_bool(self):
        self.assertEqual(type(self.heartbeat["error"]), str);