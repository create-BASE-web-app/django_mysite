from django.conf import settings
from django.db import models
from django.utils import timezone
from mdeditor.fields import MDTextField


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    snsimage = models.ImageField(upload_to='', null=True, blank=True)
    title = models.CharField(max_length=200)
    # text = models.TextField()
    text = MDTextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    good = models.IntegerField(null=True, blank=True, default=0)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
