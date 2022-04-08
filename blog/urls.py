# first we created this file with touch blog/urls.py
from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateNew, BlogUpdateView, BlogDeleteView

urlpatterns = [
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
    path('post/new/', BlogCreateNew.as_view(), name='post_new'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    path('', BlogListView.as_view(), name='home'),
]
