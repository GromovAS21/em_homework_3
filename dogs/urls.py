from django.urls import include, path
from rest_framework import routers

from dogs.apps import DogsConfig
from dogs.views import DogViewSet


app_name = DogsConfig.name

router = routers.DefaultRouter()
router.register(r"", DogViewSet, basename="dog")

urlpatterns = [
    path("", include(router.urls)),
]
