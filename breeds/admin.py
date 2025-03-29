from django.contrib import admin

from breeds.models import Breed


@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    """Админка для пород"""

    list_display = ("name", "size", "friendliness", "trainability", "shedding_amount", "exercise_needs")
    list_filter = ("size", "friendliness", "trainability", "shedding_amount", "exercise_needs")
    search_fields = ("name",)
