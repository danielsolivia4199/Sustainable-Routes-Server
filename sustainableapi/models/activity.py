from django.db import models
from .user import User
from .destination import Destination

class Activity(models.Model):
  description = models.TextField()
  location = models.ForeignKey(Destination, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  favorite = models.BooleanField()
