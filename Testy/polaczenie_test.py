import unittest
import polaczenie

class MyAppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = wynik.app.test_client()

    def test_greeting(self):
        rv = self.app.get('/')
        self.assertIn('hello', rv.data)