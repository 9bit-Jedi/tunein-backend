from django.shortcuts import render
from rest_framework import generics, status
from .serializers import Roomserializer, CreateRoomSerializer
from .models import Room
from rest_framework.views import APIView
from rest_framework.response import Response

import datetime

# Create your views here.

# GET method - getting room details
class RoomView(APIView):
  
  def get(self, request, format=None):
    rooms = Room.objects.all()
    serializer = Roomserializer(rooms, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# POST method - getting room details
class CreateRoomView(APIView):
  
  serializer_class = CreateRoomSerializer
  
  def post(self, request, format=None):
    if not self.request.session.exists(self.request.session.session_key):
      self.request.session.create()
      print('session created')
    
    serializer = CreateRoomSerializer(data=request.data)
    if serializer.is_valid(): 
      # serializer.save()
      guest_can_pause = serializer.data.get('guest_can_pause')
      votes_to_skip = serializer.data.get('votes_to_skip')
      host = self.request.session.session_key
      print(host)
      
      queryset = Room.objects.filter(host=host)
      print(queryset)
      if queryset.exists():
        print('check - room exists !')
        room = queryset[0]
        room.guest_can_pause = guest_can_pause
        room.votes_to_skip = votes_to_skip
        room.save(update_fields=['guest_can_pause', 'votes_to_skip'])
        return Response(Roomserializer(room).data, status=status.HTTP_200_OK)

      else:
        print('check - does not exists !')
        room = Room.objects.create(host=host, guest_can_pause=guest_can_pause, votes_to_skip=votes_to_skip)
        room.save()
        return Response(Roomserializer(room).data, status=status.HTTP_201_CREATED)
      
    else:       #serialiser not valid - bad reuqest error
      print('bad request')
      Response(CreateRoomSerializer(room).errors, status=status.HTTP_400_BAD_REQUEST)