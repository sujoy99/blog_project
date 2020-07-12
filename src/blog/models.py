from django.conf import settings
from django.db import models
from django.db.models import Q
from django.urls import reverse
from django.utils import timezone

User = settings.AUTH_USER_MODEL

class BlogPostQuerySet(models.QuerySet):
    def published(self):
        now = timezone.now()
        # self.get_queryset() --> BlogPost.objects
        # return self.get_queryset().filter(publish_date__lte=now)
        return self.filter(publish_date__lte=now)

    def search(self, query):
        lookup = (
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(slug__icontains=query) |
            Q(user__username__icontains=query) 
        )
        return self.filter(lookup)

class BlogPostManager(models.Manager):
    def get_queryset(self):
        return BlogPostQuerySet(self.model, using=self._db)

    def published(self):
        # now = timezone.now()
        # self.get_queryset() --> BlogPost.objects
        # return self.get_queryset().filter(publish_date__lte=now)
        return self.get_queryset().published()

    def search(self, query=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().published().search(query)

# Create your models here.
class BlogPost(models.Model): # blogpost_set --> to get blog post for any user
    user = models.ForeignKey(User, default=1,null=True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='image/', blank=True, null=True)
    title = models.CharField(max_length=120)
    slug  = models.SlugField(unique=True)
    content = models.TextField(blank=True, null=True)
    publish_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = BlogPostManager()

    class Meta:
        ordering = ['-publish_date', '-updated', '-timestamp']

    def __str__(self):
        return self.title

    def get_absolute_url(self, *args, **kwargs):
        return reverse("blog_post:blog-detail", kwargs={"slug":self.slug})
        # return f"/blog/{self.slug}"
    
    def get_edit_url(self, *args, **kwargs):
        return reverse("blog_post:blog-edit", kwargs={"slug":self.slug})
        # return f"/blog/{self.slug}"
    
    def get_delete_url(self, *args, **kwargs):
        return reverse("blog_post:blog-delete", kwargs={"slug":self.slug})
        # return f"/blog/{self.slug}"
