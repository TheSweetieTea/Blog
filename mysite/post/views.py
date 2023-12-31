from django.http import HttpRequest
from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from .models import Post, Comment
from .forms import PostForm, CommentForm, SearchForm
from django.views.decorators.http import require_POST
from django.contrib.postgres.search import SearchVector



# Create your views here.
def post_list(request):
    posts = Post.published.order_by('-create_time')

    return render(request=request,
                  template_name='post/post_list.html',
                  context={'posts': posts})


def post_detail(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    comments = post.comments.all()
    form = CommentForm()

    return render(request=request, 
                  template_name='post/post_detail.html',
                  context={
                      'post': post,
                      'form': form,
                      'comments': comments
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
                  template_name='post/forms/post_form.html',
                  context={
                      'form': form
                  })


@require_POST
def add_comment_for_post(request: HttpRequest, post_id):
    post = get_object_or_404(Post, id=post_id)

    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.author = request.user
        comment.save()

    return redirect(post.get_absolute_url())
    

def post_search(request: HttpRequest):
    form = SearchForm()
    results = []
    query = None

    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Post.published.annotate(
                search=SearchVector('title', 'text')
                ).filter(search=query)
        
    return render(request=request,
                  template_name='post/search.html',
                  context={
                      'form': form,
                      'results': results,
                      'query': query
                  })
    




