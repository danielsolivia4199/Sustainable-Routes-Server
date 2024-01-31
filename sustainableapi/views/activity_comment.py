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
        serializer = ActivityComment(activity_comments, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized comment instance
        """
        activity = Activity.objects.get(id=request.data["activity"])

        activity_comment = ActivityComment.objects.create(
            content=request.data["content"],
            activity=activity,
        )
        serializer = ActivityComment(activity_comment)
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
    """JSON serializer for game types
    """
    class Meta:
        model = ActivityComment
        fields = ('id', 'tag', 'activity')
        depth = 1
