"""View module for handling requests about activity tags"""
from django.http import HttpResponseServerError
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from sustainableapi.models import ActivityTag, Tag, Activity

class ActivityTagView(ViewSet):
    """Activity Tags"""

    def retrieve(self, request, pk):
        """Handle GET requests for single activity tag
        Returns:
            Response -- JSON serialized activity tag
        """
        activity_tag = ActivityTag.objects.get(pk=pk)
        serializer = ActivityTagSerializer(activity_tag)
        return Response(serializer.data)

    """
        def list(self, request):
            \"\"\"Handle GET requests to get all activity tags items\"\"\"
            activity_tags = ActivityTag.objects.all()
            serializer = ActivityTag(activity_tags, many=True)
            return Response(serializer.data)
    """


    @action(detail=True, methods=['get'])
    def tags_for_activity(self, request, pk=None):
        """
        Handle GET requests for tags for specific activity
        Args:
            pk (int): Primary key of the activity
        Returns:
            Response -- JSON serialized list of activity tags for specific activity
        """
        if pk is not None:
            activity_tags = ActivityTag.objects.filter(activity_id=pk)
            serializer = ActivityTagSerializer(activity_tags, many=True)
            return Response(serializer.data)
        else:
            return Response({'message': 'activity ID is required'}, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        try:
            activity = get_object_or_404(Activity, pk=request.data["activity_id"])
            tag = get_object_or_404(Tag, pk=request.data["tag_id"])          
            activity_tag = ActivityTag.objects.create(activity=activity, tag=tag)
            serializer = ActivityTagSerializer(activity_tag)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
        
    def update(self, request, pk=None):
        """Handle PUT requests to update an activity tag
        Args:
            pk (int): Primary key of the activity tag to be updated
        Returns:
            Response -- JSON serialized activity tag instance
        """
        if pk is None:
            return Response({'message': 'Activity Tag ID is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            activity_tag = get_object_or_404(ActivityTag, pk=pk)
            new_tag = get_object_or_404(Tag, pk=request.data["tagId"])
            activity_tag.tag = new_tag
            activity_tag.save()

            serializer = ActivityTagSerializer(activity_tag)
            return Response(serializer.data)
        except ValidationError as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    
    def destroy(self, request, pk=None):
        """
        Handle DELETE requests for a single activity tag
        Args:
            pk (int): Primary key of the tag to be deleted
        Returns:
            Response -- HTTP status code
        """
        try:
            activity_tag = get_object_or_404(ActivityTag, pk=pk)
            activity_tag.delete()
            return Response({'message': 'Activity Tag'}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class ActivityTagSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = ActivityTag
        fields = ('id', 'tag', 'activity')
        depth = 1
