from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class SizeChoices(models.TextChoices):
    """Модель выбора размера породы"""

    TINY = "tiny", "Маленький"
    SMALL = "small", "Малый"
    MEDIUM = "medium", "Средний"
    LARGE = "large", "Большой"


class Breed(models.Model):
    """Модель породы"""

    name = models.CharField(max_length=100, verbose_name="Название породы")
    size = models.CharField(
        max_length=50,
        choices=SizeChoices.choices,
    )
    friendliness = models.PositiveSmallIntegerField(
        verbose_name="Дружелюбие", validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    trainability = models.PositiveSmallIntegerField(
        verbose_name="Обучаемость", validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    shedding_amount = models.PositiveSmallIntegerField(
        verbose_name="Объем шерсти", validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    exercise_needs = models.PositiveSmallIntegerField(
        verbose_name="Требования к физической активности", validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    def __str__(self):
        """Строковое представление объекта класса
        Returns:
            str: название породы
        """
        return self.name

    class Meta:
        verbose_name = "Порода"
        verbose_name_plural = "Породы"
        ordering = ["name"]
