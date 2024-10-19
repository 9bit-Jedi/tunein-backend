from rest_framework import serializers
from api.models import *

# GET method - getting room details


class TrackSerializer(serializers.ModelSerializer):
  class Meta:
    model = Track
    fields = '__all__'
    
class ListenerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Listener
    fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):
  listeners = ListenerSerializer(many=True)
  current_track = TrackSerializer()
  class Meta:
    model = Room
    fields = ('code', 'host','name','description', 'listeners', 'guest_controls', 'current_track', 'current_time', 'is_playing', 'created_at')
    
# GET method - getting room details
class CreateRoomSerializer(serializers.ModelSerializer):    
  class Meta:
    model = Room
    fields = ('name','guest_controls', 'description')