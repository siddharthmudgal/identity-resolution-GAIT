import decimal

from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer, ResultSerializer
from rest_framework import viewsets

import numpy as np


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(methods=['POST'], detail=False)
    def authenticate(self, request):
        """authenticate with the data received against the user model"""
        datapacket = UserSerializer(request.data, many=False).data
        userid = datapacket['userid']
        user = get_object_or_404(User, userid=userid)
        if user is None:
            result = ResultSerializer({'result': -1}).data
            return Response(result)

        user_sensordata_x = np.array(user.sensordata_x, dtype=np.float64)
        user_sensordata_y = np.array(user.sensordata_y, dtype=np.float64)
        user_sensordata_z = np.array(user.sensordata_z, dtype=np.float64)

        sensordata_x = np.array(datapacket['sensordata_x'], dtype=np.float64)
        sensordata_y = np.array(datapacket['sensordata_y'], dtype=np.float64)
        sensordata_z = np.array(datapacket['sensordata_z'], dtype=np.float64)

        x_pearson = np.corrcoef(sensordata_x, user_sensordata_x)
        y_pearson = np.corrcoef(sensordata_y, user_sensordata_y)
        z_pearson = np.corrcoef(sensordata_z, user_sensordata_z)

        pearson_value = (x_pearson[0][1]
                         + y_pearson[0][1] + z_pearson[0][1]) / 3
        result = ResultSerializer({'corr_result':
                                   decimal.Decimal(pearson_value)}).data
        return Response(result)
