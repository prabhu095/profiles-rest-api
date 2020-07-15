from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


class HelloApiView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloSerializer

    # format is end point format here
    def get(selfS, request, format=None):
        """Returns a list of API features"""
        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs',
        ]

        return Response({
            'message': "Hello!",
            'an_apiview': an_apiview

        })

    def post(self, request):
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})

        else:
            return Response(serializer.errors,
                            status= status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handle updating an object. Here we replace the object"""

        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle partial update of object.Here we update the object"""

        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""

        return Response({'method': 'DELETE'})
