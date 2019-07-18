from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='blog_home'),
    path('post-detail/<int:post_id>/', views.PostDetail, name='post_detail'),
    path('about/', views.about, name='blog_about'),
]
