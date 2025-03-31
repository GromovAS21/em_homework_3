"""Админка для приложения пород собак."""

from django.apps import AppConfig


class BreedsConfig(AppConfig):
    """Конфигурация приложения пород собак."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "breeds"
    verbose_name = "Породы"
