from django.contrib import admin
from .models import Downvote, Post, Comment, Tag, Upvote


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    fields = ['creator', 'title', 'content']


class CommentAdmin(admin.ModelAdmin):
    fields = ['name', 'body', 'post']

class TagAdmin(admin.ModelAdmin):
    fields = ['name', 'post']

class VotingAdmin(admin.ModelAdmin):
    fields = ['post']


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Upvote, VotingAdmin)
admin.site.register(Downvote, VotingAdmin)
