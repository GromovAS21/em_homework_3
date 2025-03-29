from rest_framework import viewsets

from breeds.models import Breed
from breeds.serializers import BreedSerializer


class BreedViewSet(viewsets.ModelViewSet):
    """ Представление пород собак"""

    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
