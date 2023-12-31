from collections.abc import Iterable
from django.db import models
from django.db.models.query import QuerySet
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify


# Create your models here.

class PublishedManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)
    

class Post(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'DR', 'Draft'
        PUBLISHED = 'PB', 'Published'


    author = models.ForeignKey(User, 
                               on_delete=models.CASCADE,
                               related_name='posts')
    
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, default='')
    text = models.TextField()
    status = models.CharField(max_length=2,
                              choices=Status,
                              default=Status.PUBLISHED)
    
    create_time = models.DateTimeField(auto_now_add=timezone.now)

    objects = models.Manager()
    published = PublishedManager()

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse('post_detail', args=[self.slug])
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Comment(models.Model):
    post = models.ForeignKey(Post, 
                             on_delete=models.CASCADE,
                             related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
