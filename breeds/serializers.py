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
            "exercise_needs",
            "num_dogs",
        )


class BreedListSerializer(BreedSerializer):
    """Сериализатор для вывода списка пород собак"""

    num_dogs = serializers.SerializerMethodField()

    class Meta(BreedSerializer.Meta):
        fields = BreedSerializer.Meta.fields + ("num_dogs",)

    def get_num_dogs(self, obj):
        """Метод для подсчета количества собак данного породы"""
        if hasattr(obj, "num_dogs"):
            return obj.num_dogs
