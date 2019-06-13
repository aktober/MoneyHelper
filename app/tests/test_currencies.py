from unittest import TestCase
from django.test import Client

API_URL = '/api/currencies/'

ADMIN = {
    'username': 'admin',
    'password': 'q1234567'
}


class TestCurrenciesApi(TestCase):

    def setUp(self):
        self.client = Client()

    def test_non_authenticated(self):
        response = self.client.get(API_URL)
        assert response.status_code == 403

    def test_authenticated(self):
        self.client.login(username=ADMIN['username'],
                          password=ADMIN['password'])
        response = self.client.get(API_URL)
        assert response.status_code == 200

    def test_add(self):
        self.client.login(username=ADMIN['username'],
                          password=ADMIN['password'])
        data = {
            'code': 'usd'
        }
        response = self.client.post(API_URL, data=data)
        assert response.status_code == 200

        response = self.client.get(API_URL)
        print(response.json())
