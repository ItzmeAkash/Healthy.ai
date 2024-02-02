from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import UserRegisterSerializer

# Create your views here.

@api_view(['POST'])
def user_register_view(request):
    if request.method == 'POST':
        serializer = UserRegisterSerializer(data=request.data)
        
        data = {}
        
        if serializer.is_valid():
            account = serializer.save()
            
            data['response'] = 'Account has been created '
            data['username'] = account.username
            data['email'] = account.email
        
        else:
            serializer.errors
        
        return Response(data)