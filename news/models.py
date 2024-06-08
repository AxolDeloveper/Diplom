from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    date_create = models.DateTimeField(default=timezone.now)


    text = models.TextField(max_length=84)
    description = models.CharField(max_length=1200)

    class Meta:
        ordering = ['-date_create']

    def __str__(self):
        return self.text
