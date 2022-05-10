from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import BlockUserViewSet, ReportUserViewSet

router = DefaultRouter()
router.register("blockuser", BlockUserViewSet)
router.register("reportuser", ReportUserViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
