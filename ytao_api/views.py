# todo/todo_api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Converter
from .serializers import ConverterSerializer
from django.shortcuts import render
import youtube_dl
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def ConverterApiView(request):
	if request.method == 'GET':
		return Response(request.GET['url'])
	elif request.method == 'POST':
		return Response(request.data)