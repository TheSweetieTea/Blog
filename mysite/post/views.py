from django.http import HttpRequest
from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from .models import *
from .forms import *


# Create your views here.
def welcome(request):
    posts = Post.objects.order_by('-create_time')

    return render(request=request,
                  template_name='post/post_list.html',
                  context={'posts': posts})


def post_detail(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)

    return render(request=request, 
                  template_name='post/post_detail.html',
                  context={
                      'post': post
                  })


def add_post(request: HttpRequest):
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
        
    else:
        form = PostForm()

    return render(request=request,
                  template_name='post/add_post.html',
                  context={
                      'form': form
                  })

def test():
    pass



