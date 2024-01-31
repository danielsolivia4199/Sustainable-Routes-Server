from rest_framework import serializers
from sustainableapi.models import ActivityComment

class ActivityCommentSerializer(serializers.ModelSerializer):
  """JSON serializer for Activity Comments"""
  
  class Meta:
    model = ActivityComment
    fields = ('id', 'content')
