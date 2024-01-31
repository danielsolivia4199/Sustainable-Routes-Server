"""View module for handling requests about activity tags"""
from django.http import HttpResponseServerError
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from sustainableapi.models import DestinationComment, Destination

class DestinationCommentView(ViewSet):
    """Destination Comments"""

    def retrieve(self, request, pk):
        """Handle GET requests for single destination comment
        Returns:
            Response -- JSON serialized destination comment
        """
        destination_comment = DestinationComment.objects.get(pk=pk)
        serializer = DestinationCommentSerializer(destination_comment)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all destination comments"""
        destination_comments = DestinationComment.objects.all()
        serializer = DestinationCommentSerializer(destination_comments, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized comment instance
        """
        destination = get_object_or_404(Destination, pk=request.data.get('destinationId'))
        serializer = DestinationCommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(destination=destination)
        return Response(serializer.data)
      
    def update(self, request, pk=None):
        """Handle PUT requests to update a destination comment
        Args:
            pk (int): Primary key of the destination comment to be updated
        Returns:
            Response -- JSON serialized destination comment instance
        """
        if pk is None:
            return Response({'message': 'Comment ID is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            destination_comment = get_object_or_404(DestinationComment, pk=pk)
            serializer = DestinationCommentSerializer(destination_comment, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(serializer.data)
        except ValidationError as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        """
        Handle DELETE requests for a single comment
        Args:
            pk (int): Primary key of the comment to be deleted
        Returns:
            Response -- HTTP status code
        """
        try:
            destination_comment = get_object_or_404(DestinationComment, pk=pk)
            destination_comment.delete()
            return Response({'message': 'Comment Deleted'}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class DestinationCommentSerializer(serializers.ModelSerializer):
    """JSON serializer for comments
    """
    class Meta:
        model = DestinationComment
        fields = ('id', 'content')
        depth = 1
