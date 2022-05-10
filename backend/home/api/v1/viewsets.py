from rest_framework import viewsets
from home.models import FollowRequest, Post, PostComment, PostMedia, ReportPost
from .serializers import (
    FollowRequestSerializer,
    PostSerializer,
    PostCommentSerializer,
    PostMediaSerializer,
    ReportPostSerializer,
)
from rest_framework import authentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from home.api.v1.serializers import (
    SignupSerializer,
    UserSerializer,
)


class SignupViewSet(ModelViewSet):
    serializer_class = SignupSerializer
    http_method_names = ["post"]


class LoginViewSet(ViewSet):
    """Based on rest_framework.authtoken.views.ObtainAuthToken"""

    serializer_class = AuthTokenSerializer

    def create(self, request):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        user_serializer = UserSerializer(user)
        return Response({"token": token.key, "user": user_serializer.data})


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Post.objects.all()


class PostMediaViewSet(viewsets.ModelViewSet):
    serializer_class = PostMediaSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = PostMedia.objects.all()


class ReportPostViewSet(viewsets.ModelViewSet):
    serializer_class = ReportPostSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = ReportPost.objects.all()


class FollowRequestViewSet(viewsets.ModelViewSet):
    serializer_class = FollowRequestSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = FollowRequest.objects.all()


class PostCommentViewSet(viewsets.ModelViewSet):
    serializer_class = PostCommentSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = PostComment.objects.all()
