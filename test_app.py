import unittest
from app import app

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True 

    def test_home_status_code(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_data(self):
        response = self.app.get('/')
        self.assertTrue(b'Welcome to Flask app deployement using Jenkins.' in response.data)

    def test_aboutus_status_code(self):
        response = self.app.get('/aboutus')
        self.assertEqual(response.status_code, 200)

    def test_aboutus_data(self):
        response = self.app.get('/aboutus')
        self.assertTrue(b'This is about us page.' in response.data)

    def test_contactus_status_code(self):
        response = self.app.get('/contactus')
        self.assertEqual(response.status_code, 200)

    def test_contactus_data(self):
        response = self.app.get('/contactus')
        self.assertTrue(b'Here you can find information about how to contact us.' in response.data)

if __name__ == '__main__':
    unittest.main()
