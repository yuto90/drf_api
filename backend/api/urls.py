from django.urls import path, include
from rest_framework import routers
from api.views import BikeViewSet

router = routers.DefaultRouter()
router.register('bikes', BikeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
