from django.contrib import admin
from django.urls import path, include

admin.site.site_header = 'Администрирование "Собачек и породы"'
admin.site.site_title = "Собачки и их породы"
admin.site.index_title = "Администрирование"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/dogs/", include("dogs.urls", namespace="dogs")),
    path("api/breeds/", include("breeds.urls", namespace="breeds")),
]
