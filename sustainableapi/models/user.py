from django.db import models

class User(models.Model):
  uid = models.CharField(max_length=50)
  username = models.CharField(max_length=50)
