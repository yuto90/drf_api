from rest_framework import viewsets
from .serializers import BikeSerializer
from .models import Bike


class BikeViewSet(viewsets.ModelViewSet):
    queryset = Bike.objects.all()
    serializer_class = BikeSerializer
