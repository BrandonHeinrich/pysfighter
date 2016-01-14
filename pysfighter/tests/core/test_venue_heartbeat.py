import unittest
import pysfighter

class TestVenueHeartbeat(unittest.TestCase):
    def setUp(self):
        self.heartbeat = pysfighter.core.venue_heartbeat("TESTEX")
    
    def tearDown(self):
        del self.heartbeat
        
    def test_venue_heartbeat_has_ok(self):
        self.assertIn("ok", self.heartbeat)
        
    def test_heartbeat_ok_is_bool(self):
        self.assertEqual(type(self.heartbeat["ok"]), bool);