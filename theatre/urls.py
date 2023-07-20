from rest_framework import routers
from django.urls import path, include

from theatre.views import PlayViewSet

router = routers.DefaultRouter()
router.register("plays", PlayViewSet)

urlpatterns = [path("", include(router.urls))]

app_name = "theatre"
