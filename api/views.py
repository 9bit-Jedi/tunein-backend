from django.shortcuts import render
from rest_framework import generics, status
from .serializers import *
from .models import *
# from django.contrib.sessions.models import Session
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse

import datetime

# GET method - getting room details

class ListTracksView(APIView):
  def get(self, request, format=None):
    track = Track.objects.all()
    serializer = TrackSerializer(track, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
class ListListenersView(APIView):
  def get(self, request, format=None):
    listener = Listener.objects.all()
    serializer = RoomSerializer(listener, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

class RoomView(APIView):

  def get(self, request, format=None):
      rooms = Room.objects.all()
      serializer = RoomSerializer(rooms, many=True)
      return Response(serializer.data, status=status.HTTP_200_OK)

class GetRoom(APIView):
  serializer_class = RoomSerializer
  lookup_url_kwarg = "code"

  def get(self, request, format=None):
    code = request.GET.get(self.lookup_url_kwarg)
    print(code)
    if code != None:
      room = Room.objects.filter(code=code)
      if len(room) > 0:
        data = RoomSerializer(room[0]).data
        data["is_host"] = self.request.session.session_key == room[0].host
        return Response(data, status=status.HTTP_200_OK)
      return Response(
        {"Room Not Found": "Invalid Room Code."},
        status=status.HTTP_404_NOT_FOUND,
      )

    return Response(
      {"Bad Request": "Code paramater not found in request"},
      status=status.HTTP_400_BAD_REQUEST,
    )

# POST method - getting room details
class CreateRoomView(APIView):
  
  serializer_class = CreateRoomSerializer
  
  def post(self, request, format=None):
    if not self.request.session.exists(self.request.session.session_key):
      self.request.session.create()
    
    serializer = CreateRoomSerializer(data=request.data)
    if serializer.is_valid(): 
      guest_controls = serializer.data.get('guest_controls')
      name = serializer.data.get('name')
      listener, _ = Listener.objects.get_or_create(session_key=self.request.session.session_key)
      host = listener.session_key
      print(host)
      
      queryset = Room.objects.filter(host=host)
      if queryset.exists():
        print('check - room exists !')
        room = queryset[0]
        room.guest_controls = guest_controls
        room.name = name
        listener.room = room
        listener.save()
        room.save(update_fields=['guest_controls', 'name'])
        return Response(RoomSerializer(room).data, status=status.HTTP_200_OK)

      else:
        print('check - does not exists !')
        room = Room.objects.create(host=host, guest_controls=guest_controls, name=name)
        room.save()
        listener.room = room
        listener.save()
        return Response(RoomSerializer(room).data, status=status.HTTP_201_CREATED)
      
    else:       #serialiser not valid - bad reuqest error
      print('bad request')
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class JoinRoom(APIView):
  lookup_url_kwarg = 'code'

  def post(self, request, format=None):
    if not self.request.session.exists(self.request.session.session_key):
      self.request.session.create()

    code = request.data.get(self.lookup_url_kwarg)
    if code is not None:
      room_result = Room.objects.filter(code=code)
      if room_result.exists():
        room = room_result[0]
        self.request.session['room_code'] = code
        listener, _ = Listener.objects.get_or_create(session_key=self.request.session.session_key)
        listener.room = room
        listener.save() 
        return Response({'message': 'Room Joined!'}, status=status.HTTP_200_OK)

      return Response({'Bad Request': 'Invalid Room Code'}, status=status.HTTP_400_BAD_REQUEST)

    return Response({'Bad Request': 'Invalid post data, did not find a code key'}, status=status.HTTP_400_BAD_REQUEST)


class MyRoom(APIView):
  def get(self, request, format=None):
    if not self.request.session.exists(self.request.session.session_key):
      self.request.session.create()
    listener, _ = Listener.objects.get_or_create(session_key=self.request.session.session_key)

    data = {
      'code': self.request.session.get('room_code')
    }
    host = listener.session_key
    print(host)
    room_results = Room.objects.filter(host=host)
    print(room_results)
    serializer = RoomSerializer(room_results, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


class LeaveRoom(APIView):
  def get(self, request, format=None):
    if 'room_code' in self.request.session:
      self.request.session.pop('room_code')
      listener, _ = Listener.objects.get_or_create(session_key=self.request.session.session_key)
      listener.room = None
      listener.save()
      host = listener.session_key
      room_results = Room.objects.filter(host=host)
      if len(room_results) > 0:
        room = room_results[0]
        room.delete()
    
    return Response({'Message': 'Success'}, status=status.HTTP_200_OK)


