from django.db import models
from .tag import Tag
from .activity import Activity

class ActivityTag(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
