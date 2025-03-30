from django.db import models

from breeds.models import Breed


class GenderChoices(models.TextChoices):
    """Модель выбора пола собаки"""

    MALE = "male", "Мальчик"
    FEMALE = "female", "Девочка"


class Dog(models.Model):
    """Модель собаки"""

    name = models.CharField(max_length=100, verbose_name="Имя собаки")
    age = models.PositiveSmallIntegerField(verbose_name="Возраст собаки")
    breed = models.ForeignKey(
        Breed, on_delete=models.SET_NULL, verbose_name="Порода собаки", null=True, blank=True, related_name="dogs"
    )
    gender = models.CharField(
        max_length=10,
        choices=GenderChoices.choices,
    )
    color = models.CharField(
        max_length=100,
        verbose_name="Цвет собаки",
    )
    favorite_food = models.CharField(
        max_length=100,
        verbose_name="Любимое еда собаки",
        null=True,
        blank=True,
    )
    favorite_toy = models.CharField(
        max_length=100,
        verbose_name="Любимая игрушка собаки",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Собака"
        verbose_name_plural = "Собаки"
        ordering = ["name"]
