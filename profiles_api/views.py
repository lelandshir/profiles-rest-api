from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from profiles_api import serializers


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer
    def get(self, request, format=None):
        """Returns a list of APIViews features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your app logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message':'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message w/ your first_name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            first_name = serializer.validated_data.get('first_name')
            message = f'Hello {first_name}!'
            return Response({'message': message})
        else: 
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST 
                )

    def put(self, request, pk=None):
        """Handle updating an obj"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update of an obj"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an obj"""
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return hello message"""
        a_viewset = [
            'Uses actions ()',
            'Auto-maps to URLS using routers',
            'Provides more functionality w/ less code',
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """Create a new hello msg"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            first_name = serializer.validated_data.get('first_name')
            message = f'Hello {first_name}!'
            return Response({'message': message})
        else: 
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            ) 

    def retrieve(self, request, pk=None):
        """Handle getting an obj by ID"""
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an obj"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an obj"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an obj"""
        return Response({'http_method': 'DELETE'})