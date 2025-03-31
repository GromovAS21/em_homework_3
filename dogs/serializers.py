from rest_framework import serializers

from dogs.models import Dog


class DogSerializer(serializers.ModelSerializer):
    """Сериализатор собаки"""

    class Meta:
        model = Dog
        fields = ("id", "name", "breed", "age", "gender", "color", "favorite_food", "favorite_toy")


class DogListSerializer(DogSerializer):
    """Сериализатор для списка собак"""

    avg_age = serializers.SerializerMethodField()

    class Meta(DogSerializer.Meta):
        fields = DogSerializer.Meta.fields + ("avg_age",)

    def get_avg_age(self, obj: Dog) -> int:
        """Метод для подсчета среднего возраста собак одного вида
        Args:
            obj (Dog): экземпляр собаки
        Returns:
            int: средний возраст собак одного вида данного экземпляра
        """
        if hasattr(obj, "avg_age"):
            return obj.avg_age


class DogDetailSerializer(DogSerializer):
    """Сериализатор собаки с детальным выводом"""

    num_same_breed = serializers.SerializerMethodField()

    class Meta(DogSerializer.Meta):
        fields = DogSerializer.Meta.fields + ("num_same_breed",)

    def get_num_same_breed(self, obj: Dog) -> int:
        """Метод для подсчета количества собак одного вида данного экземпляра
        Args:
            obj (Dog): экземпляр собаки
        Returns:
            int: количество собак одного вида данного экземпляра
        """
        if hasattr(obj, "num_same_breed"):
            return obj.num_same_breed
