
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.
class Code(models.Model):
    date_create = models.DateTimeField(default=timezone.now)

    code = models.CharField()
    domain = models.CharField()

class Categories(models.Model):
    name = models.CharField(max_length=250)
    category_image = models.ImageField()

    date_crate = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

class Item(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    date_create = models.DateTimeField(default=timezone.now)

    title = models.CharField(max_length=500)
    description = models.CharField(max_length=1200)
    price = models.IntegerField()
    allowed = models.BooleanField(default=False)
    # category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    image_one = models.ImageField()
    image_two = models.ImageField()
    image_three = models.ImageField()

    class Meta:
        ordering = ['-date_create']

    def __str__(self):
        return self.title

class Profile(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    date_create = models.DateTimeField(default=timezone.now)

    description = models.CharField(max_length=250)
    balance = models.IntegerField()
    moderation_accepted = models.BooleanField()

class Rate(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Item, on_delete=models.CASCADE)

    date_create = models.DateTimeField(default=timezone.now)
    stars = models.IntegerField()


class ModerationAllow(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    date_time = models.DateTimeField(default=timezone)

    allowed = models.BooleanField(default=False)
    expire = models.IntegerField(default=365)
    status = models.CharField

class UserBasket(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
