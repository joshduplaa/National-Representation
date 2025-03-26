from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializer import UserSerializer

def index(request):
    return HttpResponse("Hello, world. You're at the starting API index.")

@api_view(['GET'])
def get_user(request):
    return Response(UserSerializer({"user": "jduplaa", "password": "abc123"}))


@api_view(['GET'])
def get_poll(request):
    return Response(UserSerializer({"title": "human rights"}))

