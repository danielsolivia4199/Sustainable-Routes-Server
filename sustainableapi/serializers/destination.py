from rest_framework import serializers
from sustainableapi.models import Destination
from .destination_comment import DestinationCommentSerializer

class DestinationSerializer(serializers.ModelSerializer):
  """JSON serializer for Destination"""
  
  comments = DestinationCommentSerializer(read_only=True, many=True)
  
  class Meta:
    model = Destination
    fields = ('id', 'image', 'name', 'description', 'comments')
