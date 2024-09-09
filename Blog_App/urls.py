from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogs_view, name='blogs'),
    path('create/', views.blog_create, name='blog_create'),
    path('<int:blog_id>', views.blog_detail_view, name='blog_detail'),
    path('<int:blog_id>/edit', views.blog_edit_view, name='blog_edit'),
    path('<int:blog_id>/delete', views.blog_delete_view, name='blog_delete'),

]
