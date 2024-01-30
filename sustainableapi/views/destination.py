"""View Model for handling requests for destinations"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from sustainableapi.models import Destination
from sustainableapi.serializers import DestinationSerializer

class DestinationView(ViewSet):
  """Sustainable Routes Destination View"""
  
  def retrieve(slef, request, pk):
    """Handle GET request for a single Destination
    
    Returns -> Response -- JSON serialized destination"""
    
    try:
      destination = Destination.objects.get(pk=pk)
      serializer = DestinationSerializer(destination)
      return Response(serializer.data)
    except Destination.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
  def list(self, reqeust):
    """Handle GET request for all orders
    
    Returns -> Response -- JSON serialized list of destinations"""
    
    destinations = Destination.objects.all()
    serializer = DestinationSerializer(destinations, many=True)
    return Response(serializer.data)
  
