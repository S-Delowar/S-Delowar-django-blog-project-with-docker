from tokenize import Comment
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from Blog_App.forms import CommentForm, PostForm
from Blog_App.models import Post

# Create your views here.

def blogs_view(request):
    blogs = Post.objects.all()
    return render(request, 'blog/blogs.html', {'blogs': blogs})

def blog_detail_view(request, blog_id):
    post = get_object_or_404(Post, pk= blog_id)
    comments = post.comments.all()
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect(f"{reverse('login')}?next={request.path}")
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.author = request.user
            new_comment.save()
            return redirect('blog_detail', blog_id = post.id)
    else:
        comment_form = CommentForm()
    
    context = {'post': post, 'comments': comments, 'comment_form': comment_form}
    return render(request, 'blog/blog_detail.html', context)

@login_required
def blog_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('blogs')
    else:
        form = PostForm()
    return render(request, 'blog/blog_create.html', {'form': form})


@login_required
def blog_edit_view(request, blog_id):
    current_blog = get_object_or_404(Post, pk=blog_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('blogs')            
    else:
        form = PostForm(instance = current_blog)
    return render(request, 'blog/blog_edit.html', {'form': form, 'current_blog': current_blog})


@login_required
def blog_delete_view(request, blog_id):
    current_blog = get_object_or_404(Post, pk=blog_id)
    if request.method == 'POST':
        current_blog.delete()
        return redirect('blogs')
    return render(request, 'blog/blog_delete_confirmation.html')
