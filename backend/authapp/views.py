from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import UserSerializer
# Create your views here.

class UserRegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            user.is_active = True
            user.save()
            
            return Response({
                'message':'Sucess'
            })
        return Response(serializer.error_messages,status.HTTP_400_BAD_REQUEST)   