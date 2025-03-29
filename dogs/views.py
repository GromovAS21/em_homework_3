from rest_framework import viewsets

from dogs.models import Dog
from dogs.serializers import DogSerializer


class DogViewSet(viewsets.ModelViewSet):
    """Представление собак"""

    queryset = Dog.objects.all()
    serializer_class = DogSerializer
