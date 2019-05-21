from unittest import TestCase
from django.test import Client

API_URL = '/api/currencies/'


class TestApi(TestCase):

    def setUp(self):
        self.client = Client()

    def test_1(self):
        response = self.client.get(API_URL)
        print(response)
        assert response.status_code == 200
