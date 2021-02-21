from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serializez a name field for testing our APIView"""
    first_name = serializers.CharField(max_length=10)