from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import BlogPost, Feedback


@admin.register(BlogPost)
class AdminBlogPost(SummernoteModelAdmin):
    list_display = ('title', 'post_type', 'created', 'modified')
    list_filter = ('post_type',)


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['subject', 'email', 'name', 'created']
