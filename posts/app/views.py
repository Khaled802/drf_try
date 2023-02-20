from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.views import View
from rest_framework import generics
from rest_framework.views import APIView

from app.permissions import CreatorOrReadOnlyPermission, PostIfCreatorPermission
from .models import ABCVoting, Downvote, Post, Comment, Tag, Upvote
from .serializer import BasePostSerializer, DownVoteSerializer, PostSerializer, CommentSerializer, CommentCreateSerializer, TagPostsSerializer, \
  TaggingPostCreationSerializer, UpVoteSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostObject(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (CreatorOrReadOnlyPermission,)


class CommentList(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer
    


class CommentObject(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (CreatorOrReadOnlyPermission,)


class Tagging(generics.CreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TaggingPostCreationSerializer
    permission_classes = (PostIfCreatorPermission,)


class UnTagging(generics.DestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TaggingPostCreationSerializer
    lookup_field = 'name'
    permission_classes = (PostIfCreatorPermission,)

    def perform_destroy(self, instance: Tag):
        serializer = self.serializer_class(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        post = get_object_or_404(Post, id=self.request.data['post_id'])
        instance.post.remove(post)
        return Response(status=status.HTTP_204_NO_CONTENT)


    

class TagPosts(generics.RetrieveAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagPostsSerializer
    lookup_field = 'name'


class VotingManager(APIView):
    serializer_class = UpVoteSerializer
    model = Upvote

    @classmethod
    def check_valition_data(cls, request):
        serializer = cls.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

    @classmethod
    def get_post(cls, request) -> Post:
        post_id = request.data['post_id']
        return get_object_or_404(Post, id=post_id)
    
    @classmethod
    def get_voter(cls, request) -> Post:
        voter_id = request.data['voter_id']
        return get_object_or_404(User, id=voter_id)

    @classmethod
    def normalizer_for_related(cls, post, voter, model: ABCVoting):
        print(model)
        try:
            return model.objects.get(post=post, voter=voter)
        except Exception as e:
            print(e)
            return None

    @classmethod
    def get_up_down_vote(cls, post, voter):
        return cls.normalizer_for_related(post, voter, Upvote), cls.normalizer_for_related(post, voter, Downvote)
    
    @classmethod
    def perform_post_voting(cls, obj: ABCVoting, post: Post, voter:User, successed_created: str, successed_removed: str, rev: ABCVoting):
        if obj is None:
            if rev:
                rev.delete()
            obj = cls.model.objects.create(post=post, voter=voter)
            return Response({'detail': successed_created}, status=status.HTTP_201_CREATED)

        obj.delete()
        return Response({'detail': successed_removed}, status=status.HTTP_204_NO_CONTENT)


class UpAndUnVote(VotingManager):
    serializer_class = UpVoteSerializer
    model = Upvote

    def post(self, request):
        self.check_valition_data(request)
        post = self.get_post(request)
        voter = request.user
        
        upvote, downvote = self.get_up_down_vote(post, voter)

        return self.perform_post_voting(upvote, post, voter, successed_created='upvoted',
                        successed_removed='un upvoted', rev=downvote)

class DownAndUnVote(VotingManager):
    serializer_class = DownVoteSerializer
    model = Downvote

    def post(self, request):
        self.check_valition_data(request)
        post = self.get_post(request)
        voter = request.user
        upvote, downvote = self.get_up_down_vote(post, voter)
        return self.perform_post_voting(downvote, post, voter, successed_created='downvoted',
                        successed_removed='un downvoted', rev=upvote)