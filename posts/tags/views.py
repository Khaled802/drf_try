from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import PostsTag
# Create your views here.

class TagManger:

    @classmethod
    def get_tag_or_none(cls, request):
        return request.data.get('tag')
    
    @classmethod
    def get_response_request_not_have_tag(cls):
        return Response({'details': 'the tag is not in the request'}, status=status.HTTP_400_BAD_REQUEST)
    
    @classmethod
    def get_id_response(cls, ids: list, cls_name: str):
        return Response({cls_name: ids}, status=status.HTTP_200_OK)
    
class PostTagView(APIView):

    def get(self, request):
        tag = TagManger.get_tag_or_none(request)
        if not tag:
            return TagManger.get_response_request_not_have_tag()
        
        return TagManger.get_id_response(PostsTag.get_ids(tag), PostsTag.get_class_name())

