from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    DownvotePostViewSet,
    FollowRequestViewSet,
    LikeCommentViewSet,
    PostViewSet,
    PostCommentViewSet,
    PostMediaViewSet,
    ReportPostViewSet,
    UpvotePostViewSet,
)

from home.api.v1.viewsets import (
    SignupViewSet,
    LoginViewSet,
)

router = DefaultRouter()
router.register("signup", SignupViewSet, basename="signup")
router.register("login", LoginViewSet, basename="login")
router.register("post", PostViewSet)
router.register("postmedia", PostMediaViewSet)
router.register("reportpost", ReportPostViewSet)
router.register("followrequest", FollowRequestViewSet)
router.register("postcomment", PostCommentViewSet)
router.register("likecomment", LikeCommentViewSet)
router.register("upvotepost", UpvotePostViewSet)
router.register("downvotepost", DownvotePostViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
