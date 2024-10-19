from rest_framework import serializers
from api.models import Room

# GET method - getting room details
class Roomserializer(serializers.ModelSerializer):    
  class Meta:
    model = Room
    fields = ('id', 'code', 'host', 'guest_can_pause', 'votes_to_skip')
    
# GET method - getting room details
class CreateRoomSerializer(serializers.ModelSerializer):    
  class Meta:
    model = Room
    fields = ('guest_can_pause', 'votes_to_skip')