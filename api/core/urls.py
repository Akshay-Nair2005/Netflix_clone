from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet,
    MovieViewSet,
    SeriesViewSet,
    EpisodeViewSet,
    SeasonViewSet,
)

router = DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"movies", MovieViewSet)
router.register(r"series", SeriesViewSet)
router.register(r"episodes", EpisodeViewSet)
router.register(r"seasons", SeasonViewSet)

urlpatterns = [
    path("", include(router.urls)),
]