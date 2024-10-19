from django.urls import path
from .views import RoomView, CreateRoomView

urlpatterns = [
    path('', RoomView.as_view()),
    path('create/', CreateRoomView.as_view()),
    # join room path t.b.a.
]
