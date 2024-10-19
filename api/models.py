from django.db import models

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

class Room(models.Model):
  code = models.CharField(max_length=8, default=generate_random_code, unique=True)
  host = models.CharField(max_length=50, unique=True)
  guest_can_pause = models.BooleanField(null=False, default=False)
  votes_to_skip = models.IntegerField(null=False, default=1)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
      return self.code