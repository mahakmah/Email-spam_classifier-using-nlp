import unittest
from app import app  # Import your Flask app

class TestEmailSpamClassifierApp(unittest.TestCase):
    
    def setUp(self):
        """ Set up the test environment """
        self.client = app.test_client()  # Using Flask's test client
    
    def test_home_page(self):
        """ Test if the home page is accessible """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Spam Classifier Backend is running", response.data)
    
    def test_spam_prediction(self):
        """ Test if the app correctly classifies a spam email """
        spam_email = {
            'email': 'You have won a free iPhone! Claim now.'
        }
        response = self.client.post('/predict', json=spam_email)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Spam', response.data)
    
    def test_ham_prediction(self):
        """ Test if the app correctly classifies a ham email """
        ham_email = {
            'email': 'Let’s meet at 5 PM to discuss the project.'
        }
        response = self.client.post('/predict', json=ham_email)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Not Spam', response.data)

    def test_no_input(self):
        """ Test if the app handles missing input """
        response = self.client.post('/predict', json={})
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'No input provided', response.data)

if __name__ == '__main__':
    unittest.main()
