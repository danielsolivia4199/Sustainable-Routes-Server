from rest_framework import serializers
from sustainableapi.models import DestinationComment

class DestinationCommentSerializer(serializers.ModelSerializer):
  """JSON serializer for Destination Comments"""
  
  class Meta:
    model = DestinationComment
    fields = ('id', 'content')
