from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Post(models.Model):
    author_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=30, unique=True)
    text = models.TextField()
    link = models.URLField(max_length=128, db_index=True, unique=True, blank=True)
    date = models.DateTimeField(auto_now=True)
    upVotes = models.PositiveIntegerField(0)

    def get_absolute_url(self):
        return reverse('post_edit', kwargs={'pk': self.pk})


class Comments(models.Model):
    author_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(verbose_name="текст комментария")
    creation_date = models.DateTimeField(auto_now=True)
    comments_post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)

    class Meta():
        db_table = "comments"