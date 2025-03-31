"""Представление пород собак."""

from typing import Type

from django.db.models import Count
from rest_framework import viewsets

from breeds.models import Breed
from breeds.serializers import BreedListSerializer, BreedSerializer


class BreedViewSet(viewsets.ModelViewSet):
    """Представление пород собак."""

    queryset = Breed.objects.annotate(num_dogs=Count("dogs"))

    def get_serializer_class(self) -> Type[BreedSerializer]:
        """Возвращаем сериализаторы в зависимости от действия.

        Returns:
            Class: сериализатор для модели Breed
        """
        if self.action == "list":
            return BreedListSerializer
        return BreedSerializer
