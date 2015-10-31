from app import app
import unittest


class FlaskTestCase(unittest.TestCase):
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_login_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertTrue(b'Login now' in response.data)

    def test_login_with_right_credentials(self):
        tester = app.test_client(self)
        response = tester.post('/login', data=dict(username='admin', password='admin'), follow_redirects=True)
        self.assertIn(b'Hello To my home', response.data)

    def test_login_with_wrong_credentials(self):
        tester = app.test_client(self)
        response = tester.post('/login', data=dict(username='adsfasd', password='vzxcv'), follow_redirects=True)
        self.assertIn(b'Invalid credentials', response.data)

    def test_logout(self):
        tester = app.test_client(self)
        tester.post('/login', data=dict(username='admin', password='admin'), follow_redirects=True)
        response = tester.get('/logout', follow_redirects=True)
        self.assertIn(b'You logged out!', response.data)

if __name__ == '__main__':
    unittest.main()
