from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(default='')
    photo = models.ImageField(upload_to='blog_photos')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)  
    
    def __str__(self):
        return self.title[:20]
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=350)
    created_at = models.DateTimeField(default=timezone.now)  
    
    def __str__(self):
        return f'Comment by {self.author} on {self.post}'
    