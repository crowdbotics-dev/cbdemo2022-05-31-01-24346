from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import BlockUserViewSet

router = DefaultRouter()
router.register("blockuser", BlockUserViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
