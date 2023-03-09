
from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from .serializers import EventSerializer, ImageEventSerilizer
from .helper import GoingEvent
from .models import Event, EventImage
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
class EventList(generics.ListCreateAPIView):
    queryset = Event.get_comming_and_current()
    serializer_class = EventSerializer

class EventListAll(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class GoingView(APIView):
    def post(self, request):
        event_id = request.data.get('event_id', None)
        if event_id is None:
            return Response({'detail': "should provide event_id"}, status=status.HTTP_400_BAD_REQUEST)

        going = GoingEvent(request.user, event_id=event_id)
        if not going.is_there_error:
            going.press()
        
        message, state = going.message_list.get_top()
        return Response({'details': message}, status=state)
    


class ImageEventCreate(generics.CreateAPIView):
    queryset = EventImage.objects.all()
    serializer_class = ImageEventSerilizer

class ImageEventObject(generics.RetrieveAPIView):
    cqueryset = EventImage.objects.all()
    serializer_class = ImageEventSerilizer


        



