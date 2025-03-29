from rest_framework import serializers

from breeds.models import Breed


class BreedSerializer(serializers.ModelSerializer):
    """Сериализатор для пород собак"""

    class Meta:
        model = Breed
        fields = (
            "id",
            "name",
            "size",
            "friendliness",
            "trainability",
            "shedding_amount",
            "exercise_needs"
        )

