from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    create_time = models.DateTimeField(auto_now_add=timezone.now)

    def __str__(self) -> str:
        return self.name
