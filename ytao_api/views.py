# todo/todo_api/views.py
# from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework import status
from rest_framework.parsers import JSONParser
# from .models import Converter
# from .serializers import ConverterSerializer
from django.shortcuts import render
import youtube_dl
from rest_framework.decorators import api_view, parser_classes


@api_view(['GET', 'POST'])
@parser_classes([JSONParser])
def ConverterApiView(request):
	if request.method == 'GET':
		k=youtube_dl.YoutubeDL({'format': 'bestaudio'})
		audio_source=k.extract_info(request.GET['url'], download=False)['formats'][0]['url']
		return Response({'url': audio_source})
	elif request.method == 'POST':
		return Response(request.data)