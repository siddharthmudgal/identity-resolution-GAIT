import json
from unittest import TestCase

from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

USERS_URL = reverse('core:users-authenticate')


class TestPublicApisUser(TestCase):
    """test authenticate API"""

    def setUp(self):
        self.client = APIClient()

    def test_authenticate_flow_invalid_user(self):
        """test authenticate rest API with invalid username"""

        payload = {'userid': 'hello345',
                   'sensordata_x': [
                       '5.00000',
                       '2.00000',
                       '3.00000',
                       '5.00000'
                   ],
                   'sensordata_y': [
                       '5.00000',
                       '2.00000',
                       '3.00000',
                       '5.00000'
                   ],
                   'sensordata_z': [
                       '5.00000',
                       '2.00000',
                       '3.00000',
                       '5.00000'
                   ],
                   }
        res = self.client.post(USERS_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)

    def test_authenticate_flow_valid_user(self):
        """test authenticate rest API with valid username"""
        payload = {
            'userid': 'sampleuserid',
            'sensordata_x': [
                '5.00000',
                '2.00000',
                '3.00000',
                '5.00000'
            ], 'sensordata_y': [
                '5.00000',
                '2.00000',
                '3.00000',
                '5.00000'
            ], 'sensordata_z': [
                '5.00000',
                '2.00000',
                '3.00000',
                '5.00000'
            ],
        }

        res = self.client.post(USERS_URL,
                               data=json.dumps(payload),
                               content_type='application/json')

        self.assertEqual(res.status_code, status.HTTP_200_OK)
