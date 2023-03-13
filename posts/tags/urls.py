from django.urls import path

from .views import PostTagView

urlpatterns = [
    path('posts/', PostTagView.as_view()),
]