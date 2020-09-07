from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Bio = models.TextField(default='No Bio', max_length=300)
    email = models.EmailField(max_length=200)
    country = models.CharField(max_length=200, blank=True)
    # friends
    associates = models.ManyToManyField(User, blank=True, related_name='associates')
    slug = models.SlugField(unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}-{self.created}"
