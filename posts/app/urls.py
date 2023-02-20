from django.urls import path

from .views import DownAndUnVote, PostList, PostObject, CommentList, CommentObject, TagPosts, \
    Tagging, UnTagging, UpAndUnVote

urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>/', PostObject.as_view()),
    path('comments/', CommentList.as_view()),
    path('comments/<int:pk>/', CommentObject.as_view()),
    path('tags/', Tagging.as_view()),
    path('tags/<str:name>/delete/', UnTagging.as_view()),
    path('tags/<str:name>/', TagPosts.as_view()),
    path('upvote/', UpAndUnVote.as_view()),
    path('downvote/', DownAndUnVote.as_view()),
]
