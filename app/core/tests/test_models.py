from unittest import TestCase
from ..models import User


class TestUser(TestCase):
    def test_createUserModel(self):
        """test to see if user model is getting created properly"""
        sensordata = [1.2, 2.0, 3.5, 5.6]

        user = User.objects.create(
            userid="sampleuserid",
            sensordata_x=sensordata,
            sensordata_y=sensordata,
            sensordata_z=sensordata,
        )

        self.assertEqual(user.__str__(), "sampleuserid")
