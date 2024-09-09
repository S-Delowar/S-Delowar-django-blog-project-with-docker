from django import forms

from Blog_App.models import Comment, Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'photo']
        

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']