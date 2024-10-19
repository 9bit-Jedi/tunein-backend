from django.urls import path
from .views import *

urlpatterns = [
    path('list/', RoomView.as_view()),
    path('create/', CreateRoomView.as_view()),
    path('join/', JoinRoom.as_view()),
    path('get/', GetRoom.as_view()),
    path('my-room/', MyRoom.as_view()),
    path('leave/', LeaveRoom.as_view()),
]
