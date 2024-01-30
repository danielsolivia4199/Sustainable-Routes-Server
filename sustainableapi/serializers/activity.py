from rest_framework import serializers
from sustainableapi.models import Activity
from .activity_comment import ActivityCommentSerializer

class ActivitySerializer(serializers.ModelSerializer):
  """JSON serializer for Activities"""
  
  comments = ActivityCommentSerializer(read_only=True, many=True)
  
  class Meta:
    model = Activity
    fields = ('id', 'description', 'location', 'user', 'favorite', 'comments')
    depth = 1
