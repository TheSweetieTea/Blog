from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='home'),
    path('post/<slug:post_slug>/', views.post_detail, name='post_detail'),
    path('add_post/', views.add_post, name='addpost'),
    path('add_comment/<int:post_id>/', views.add_comment_for_post, name='post_comment'),
    path('search/', views.post_search, name='post_search')
]