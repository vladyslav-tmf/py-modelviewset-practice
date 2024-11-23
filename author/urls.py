from django.urls import path, include
from rest_framework import routers
from author import views


app_name = "author"

router = routers.DefaultRouter()
router.register("authors", views.AuthorViewSet, basename="manage")

urlpatterns = [path("", include(router.urls))]
