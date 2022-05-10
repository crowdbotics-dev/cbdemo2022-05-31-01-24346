from rest_framework import authentication
from users.models import BlockUser
from .serializers import BlockUserSerializer
from rest_framework import viewsets


class BlockUserViewSet(viewsets.ModelViewSet):
    serializer_class = BlockUserSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = BlockUser.objects.all()
