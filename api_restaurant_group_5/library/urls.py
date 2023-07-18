from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import BookCreateFromGoogleAPI, BookSearchAPI

app_name = "book"

router = DefaultRouter()
router.register("", BookSearchAPI, basename="book"),

urlpatterns = [
    path("", include(router.urls)),
    path("google", BookCreateFromGoogleAPI.as_view(), name="book-create"),
]
