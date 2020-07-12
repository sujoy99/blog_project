from django.db import models
from django.conf import settings
# Create your models here.

user = settings.AUTH_USER_MODEL 

class SearchQuery(models.Model):
    user = models.ForeignKey(user, blank=True, null=True, on_delete=models.SET_NULL)
    query = models.CharField(max_length=220)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)
