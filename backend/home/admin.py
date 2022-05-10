from django.contrib import admin
from .models import (
    FollowRequest,
    LikeComment,
    Post,
    PostComment,
    PostMedia,
    ReportPost,
    UpvotePost,
)

admin.site.register(Post)
admin.site.register(PostMedia)
admin.site.register(ReportPost)
admin.site.register(FollowRequest)
admin.site.register(PostComment)
admin.site.register(LikeComment)
admin.site.register(UpvotePost)

# Register your models here.
