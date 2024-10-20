from django.urls import path
from .views import *

urlpatterns = [
    path('list-tracks/', ListTracksView.as_view()),
    path('list-listeners/', ListListenersView.as_view()),
    path('list-rooms/', RoomView.as_view()),
    path('create-room/', CreateRoomView.as_view()),
    path('join-room/', JoinRoom.as_view()),
    path('get-room/', GetRoom.as_view()),
    path('my-room/', MyRoom.as_view()),
    path('leave-room/', LeaveRoom.as_view()),
]
