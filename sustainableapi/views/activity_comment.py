"""View module for handling requests about activity tags"""
from django.http import HttpResponseServerError
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from sustainableapi.models import ActivityComment, Activity

class ActivityCommentView(ViewSet):
    """Activity Comments"""

    def retrieve(self, request, pk):
        """Handle GET requests for single activity comment
        Returns:
            Response -- JSON serialized activity comment
        """
        activity_comment = ActivityComment.objects.get(pk=pk)
        serializer = ActivityCommentSerializer(activity_comment)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all activity comments"""
        activity_comments = ActivityComment.objects.all()
        serializer = ActivityCommentSerializer(activity_comments, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized comment instance
        """
        # Get the activity object. Use get_object_or_404 to handle cases where the activity does not exist.
        activity = get_object_or_404(Activity, pk=request.data.get('activityId'))

        # Initialize the serializer with data and the activity instance
        serializer = ActivityCommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Save the new ActivityComment instance using validated data
        # Pass the activity instance to the save method
        serializer.save(activity=activity)

        # Return the serialized new ActivityComment instance
        return Response(serializer.data)
    
    def destroy(self, request, pk=None):
        """
        Handle DELETE requests for a single comment
        Args:
            pk (int): Primary key of the tag to be deleted
        Returns:
            Response -- HTTP status code
        """
        try:
            activity_comment = get_object_or_404(ActivityComment, pk=pk)
            activity_comment.delete()
            return Response({'message': 'Comment'}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class ActivityCommentSerializer(serializers.ModelSerializer):
    """JSON serializer for comments
    """
    class Meta:
        model = ActivityComment
        fields = ('id', 'content', 'activity')
        depth = 1
