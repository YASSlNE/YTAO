from rest_framework import serializers
# from .models import Converter
class ConverterSerializer(serializers.Serializer):
    url = serializers.CharField(max_length=1000)
