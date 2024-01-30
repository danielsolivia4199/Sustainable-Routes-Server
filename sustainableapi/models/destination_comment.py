from django.db import models
from .destination import Destination

class DestinationComment(models.Model):
  content = models.TextField()
  destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
