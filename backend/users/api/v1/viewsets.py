from rest_framework import authentication
from users.models import BlockUser, ReportUser
from .serializers import BlockUserSerializer, ReportUserSerializer
from rest_framework import viewsets


class BlockUserViewSet(viewsets.ModelViewSet):
    serializer_class = BlockUserSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = BlockUser.objects.all()


class ReportUserViewSet(viewsets.ModelViewSet):
    serializer_class = ReportUserSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = ReportUser.objects.all()
