from django.contrib import admin
from .models import Post, PostMedia, ReportPost

admin.site.register(Post)
admin.site.register(PostMedia)
admin.site.register(ReportPost)

# Register your models here.
