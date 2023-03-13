
from rest_framework import serializers

from .models import Event, EventImage


class EventSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField(read_only=True)
    users_going_ids = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'start_at', 'end_at', 'going', 'images', 'users_going_ids']
    
    def get_images(self, obj: Event):
        images = obj.event_images.all()
        serializers = ImageEventSerilizer(images, many=True)
        return serializers.data
    
    def get_users_going_ids(self, obj: Event):
        return list(obj.event_going.values('user_id'))
    

class ImageEventSerilizer(serializers.ModelSerializer):
    image = serializers.ImageField()
    event_id = serializers.IntegerField()

    class Meta:
        model = EventImage
        fields = ['image', 'event_id']

