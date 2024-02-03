from django.db import models
from .user import User
from .destination import Destination

class Activity(models.Model):
  description = models.TextField()
  location = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name="activities")
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  favorite = models.BooleanField()
