from rest_framework import serializers

from dogs.models import Dog


class DogSerializer(serializers.ModelSerializer):
    """Сериализатор собаки"""

    class Meta:
        model = Dog
        fields = ("id", "name", "breed", "gender", "color", "favorite_food", "favorite_toy")
