"""конфигурация приложения собак."""

from django.apps import AppConfig


class DogsConfig(AppConfig):
    """Конфигурация приложения собак."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "dogs"
    verbose_name = "Собаки"
