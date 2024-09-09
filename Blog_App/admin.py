from django.contrib import admin

from Blog_App.models import Comment, Post

# Register your models here.

class CommentInline(admin.TabularInline):
    model = Comment

class PostAdmin(admin.ModelAdmin):
    inlines = [CommentInline,]

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)