"""View module for handling requests for activities"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from sustainableapi.models import Activity, User, Destination
from sustainableapi.serializers import ActivitySerializer

class ActivityView(ViewSet):
  """Sustainable Routes Activity View"""
  
  def retrieve(self, request, pk):
    """Handle GET request for a single activity
    
    Returns -> Response -- JSON serialized activity"""
    
    try:
      activity = Activity.objects.get(pk=pk)
      serializer = ActivitySerializer(activity)
      return Response(serializer.data)
    except Activity.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
  def list(self, request):
    """Handle GET reqeust for all activities
    
    Returns -> Response --JSON serialized list of activities"""
    
    activities = Activity.objects.all()
    serializer = ActivitySerializer(activities, many=True)
    return Response(serializer.data)
  
  def create(self, request):
    """Handle POST request for activities
    
    Returns -> JSON serialized activity instance with a 201 statue"""
    
    user = User.objects.get(pk=request.data['user'])
    location = Destination.objects.get(pk=request.data['location'])
    
    activity = Activity.objects.create(
      description = request.data['description'],
      location = location,
      user = user,
      favorite = request.data['favorite']
    )
    
    serializer = ActivitySerializer(activity)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  
  def update(self, request, pk):
    """Handles PUT requests for an activity
    
    Returns -> JSON serialized activity instance with a 200 status"""
    
    
    user = User.objects.get(pk=request.data['user'])
    location = Destination.objects.get(pk=request.data['location'])
    
    activity = Activity.objects.get(pk=pk)
    
    activity.description = request.data['description']
    activity.location = location
    activity.user = user
    activity.favorite = request.data['favorite']
    
    activity.save()
    serializer = ActivitySerializer(activity)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  def destroy(self, request, pk):
    """Handles Delete requests for an activity
    
    Returns -> Empy body with a 204 status"""
    
    activity = Activity.objects.get(pk=pk)
    activity.delete()
    return Response(None, status=status.HTTP_204_NO_CONTENT)
    