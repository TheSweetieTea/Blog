from django.urls import path
from . import views


urlpatterns = [
    path('', views.welcome, name='home'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('addpost/', views.add_post, name='addpost')
]