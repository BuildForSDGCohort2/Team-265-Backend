from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.
User = settings.AUTH_USER_MODEL

class PostQuerySet(models.QuerySet):
     def published(self):
        now = timezone.now()
        return self.filter(publish_date__lte=now)


class PostManager(models.Manager):
    def get_queryset(self):
        return PostQuerySet(self.model, using=self._db)

class Post(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField(null=True, blank=True)
    publish_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    objects = PostManager()

    class Meta:
        ordering = ['-publish_date', '-updated', '-timestamp']

    def get_absolute_url(self):
        return f"/post/{self.slug}"

    def get_edit_url(self):
        return f"{self.get_absolute_url()}/edit"
        #return f"/blog/{self.slug}/edit"
        #return f"/blog"

    def get_delete_url(self):
        return f"{self.get_absolute_url()}/delete"
        #return f"/blog/{self.slug}/delete"

    def get_create_url(self):
        return f"/new-post"

    def get_view_all_url(self):
        return f"/post"


class Blog:
    title = "My Title"
    content = "My content"