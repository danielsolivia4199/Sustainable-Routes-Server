from django.db import models

class Destination(models.Model):
  image = models.CharField(max_length=200)
  name = models.CharField(max_length=50)
  description = models.TextField()
  