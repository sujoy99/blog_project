from django.conf import settings
from django.db import models
from django.urls import reverse

User = settings.AUTH_USER_MODEL

# Create your models here.
class BlogPost(models.Model): # blogpost_set --> to get blog post for any user
    user = models.ForeignKey(User, default=1,null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=120)
    slug  = models.SlugField(unique=True)
    content = models.TextField(blank=True, null=True)

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
