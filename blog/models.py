from django.conf import settings
from django.db import models
from django.utils import timezone
from mdeditor.fields import MDTextField
from markdown import markdown
from django.utils.html import mark_safe

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
    
    def get_text_as_markdown(self):
        return mark_safe(markdown(self.text, safe_mode='escape'))

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    user_name = models.CharField('名前', max_length=255, default='名無し')
    message = models.TextField('本文')
    target = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='対象記事')
    created_at = models.DateTimeField('作成日', default=timezone.now)

    def __str__(self):
        return self.message[:20]
