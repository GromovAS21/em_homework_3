"""Настройки админ-панели для собак."""

from django.contrib import admin

from dogs.models import Dog


@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    """Админка для собак."""

    list_display = ("id", "name", "age", "breed", "gender", "color", "favorite_food", "favorite_toy")
    list_filter = ("breed", "gender", "color")
    search_fields = ("name",)
