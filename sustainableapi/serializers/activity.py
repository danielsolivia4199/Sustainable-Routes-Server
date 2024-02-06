from rest_framework import serializers
from sustainableapi.models import Activity, ActivityTag
from .activity_comment import ActivityCommentSerializer

class ActivityTagSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = ActivityTag
        fields = ('id', 'tag',)
        depth = 1

class ActivitySerializer(serializers.ModelSerializer):
  """JSON serializer for Activities"""
  
  comments = ActivityCommentSerializer(read_only=True, many=True)
  tags = ActivityTagSerializer(read_only=True, many=True)
  
  class Meta:
    model = Activity
    fields = ('id', 'description', 'location', 'user', 'favorite', 'comments', 'tags')
    depth = 1
