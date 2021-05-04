from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet


router = routers.DefaultRouter()
router.register('users', UserViewSet)

app_name = 'core'

urlpatterns = [
    path('', include(router.urls)),
]
