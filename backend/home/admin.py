from django.contrib import admin
from .models import FollowRequest, Post, PostMedia, ReportPost

admin.site.register(Post)
admin.site.register(PostMedia)
admin.site.register(ReportPost)
admin.site.register(FollowRequest)

# Register your models here.
