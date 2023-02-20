from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Commentable(models.Model):

    class Meta:
        abstruct = True

class Comment(models.Model):
    post = models.ForeignKey(Commentable, on_delete=models.CASCADE, related_name='commetable_comments')
    body = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comments', default=1)
    date_posted = models.DateTimeField(auto_now_add=True)
    date_last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} -> {self.post}'