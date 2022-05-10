from django.contrib import admin
from .models import FollowRequest, Post, PostComment, PostMedia, ReportPost

admin.site.register(Post)
admin.site.register(PostMedia)
admin.site.register(ReportPost)
admin.site.register(FollowRequest)
admin.site.register(PostComment)

# Register your models here.
