from django.urls import include, path
from rest_framework import routers

from breeds.apps import BreedsConfig
from breeds.views import BreedViewSet


app_name = BreedsConfig.name

router = routers.DefaultRouter()
router.register(r"", BreedViewSet, basename="breed")

urlpatterns = [
    path("", include(router.urls)),
]
