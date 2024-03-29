from django.urls import path

from .views import DownAndUnVote, PostList, PostObject, CommentList, CommentObject, ReplyList, ReplyObject, UpAndUnVote, LoveView, VotingState

urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>/', PostObject.as_view()),
    path('comments/', CommentList.as_view()),
    path('comments/<int:pk>/', CommentObject.as_view()),
    path('comments/reply/', ReplyList.as_view()),
    path('comments/reply/<int:pk>/', ReplyObject.as_view()),
    path('comments/love/', LoveView.as_view()),
    path('upvote/', UpAndUnVote.as_view()),
    path('downvote/', DownAndUnVote.as_view()),
    path('voting_state/', VotingState.as_view()),
]
