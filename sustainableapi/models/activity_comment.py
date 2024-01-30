from django.db import models
from .activity import Activity

class ActivityComment(models.Model):
  content = models.TextField()
  activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
