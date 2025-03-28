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
    return Response(UserSerializer({"name": "jduplaa", "password": "abc123"}).data)

@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def get_poll(request):
    return Response(UserSerializer({"title": "human rights"}).data)

@api_view(['POST'])
def get_poll(request):
    return Response(UserSerializer({"title": "human rights"}).data)

