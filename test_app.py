import unittest
from app import app
import werkzeug

# Patch temporário para adicionar o atributo '__version__' em werkzeug
if not hasattr(werkzeug, '__version__'):
    werkzeug.__version__ = "mock-version"

class APITestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
    
        cls.client = app.test_client()
    def test_nonexistent_route(self):
        response = self.client.get('/rota-invalida')
        self.assertEqual(response.status_code, 404)


    def test_get_items(self):
        response = self.client.get('/items')
        self.assertEqual(response.status_code, 200)
        self.assertIn("items", response.json)
        self.assertIsInstance(response.json["items"], list)

    def test_login(self):
        response = self.client.post('/login')
        self.assertEqual(response.status_code, 200)
        self.assertIn("access_token", response.json)
        self.token = response.json["access_token"]

if __name__ == '__main__':
    unittest.main()
