from django.shortcuts import render
from django.shortcuts import render_to_response
from django.conf import settings

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from rest_framework import authentication, permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class UserCreate(APIView):
    def post(self, request):
        username = request.data.get('username', '')
        password = request.data.get('password', '')
        User.objects.create_user(username, password=password)
        return Response(status=status.HTTP_201_CREATED)


class UserLogin(APIView):
    def post(self, request):
        username = request.data.get('username', '')
        password = request.data.get('password', '')
        user = authenticate(username=username, password=password)
        login(request, user)
        return Response(status=status.HTTP_200_OK)


class UserLogout(APIView):
    def get(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)


