from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_posts', default=1)
    date_posted = models.DateTimeField(auto_now_add=True)
    date_last_update = models.DateTimeField(auto_now=True)


    @property
    def creator_id(self):
        return self.creator.id
    @property
    def upvotes(self):
        return self.post_upvote.all().count()
    
    @property
    def downvotes(self):
        return self.post_downvote.all().count()

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comments')
    body = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comments', default=1)
    date_posted = models.DateTimeField(auto_now_add=True)
    date_last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} -> {self.post}'


class Tag(models.Model):
    post = models.ManyToManyField(Post, related_name='post_tags')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ABCVoting(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    voter = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        abstract = True

    def __str__(self) -> str:
        return f'post:{self.post}, voter:{self.voter}'


class Upvote(ABCVoting):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_upvote')
    voter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='voter_upvote', default=1)


class Downvote(ABCVoting):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_downvote')
    voter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='voter_downvote', default=1)
    

