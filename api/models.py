from django.db import models

import redis
from django.conf import settings
# redis_instance = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0)

import string
import random

def generate_random_code():
  # return 876545
  length=5
  while True:
    code = ''.join(random.choices(string.digits+string.ascii_uppercase, k=length))
    print(code)
    if not Room.objects.filter(code=code).exists():
      break
  return code

# Create your models here.

class Listener(models.Model):
  session_key = models.CharField(max_length=128, unique=True)
  room = models.ForeignKey('Room', on_delete=models.CASCADE, null=True, related_name='listeners')
  control_permission = models.BooleanField(default=False)
  
  def __str__(self): 
    return self.session_key
  
class Track(models.Model):
  title = models.CharField(max_length=128, unique=True)
  file = models.FileField(upload_to='tracks')
  def __str__(self): 
    return self.title

class Room(models.Model):
  code = models.CharField(max_length=8, default=generate_random_code, unique=True)
  name = models.CharField(max_length=50, default="Room Name")
  description = models.TextField(null=True, blank=True)
  host = models.CharField(max_length=50, unique=True)
  guest_controls = models.BooleanField(null=False, default=False)
  
  current_track = models.ForeignKey('Track', on_delete=models.CASCADE, null=True) 
  current_time = models.FloatField(default=0.0)
  is_playing = models.BooleanField(default=False) 
  
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
      return self.code