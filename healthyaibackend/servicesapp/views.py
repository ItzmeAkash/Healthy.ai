from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import DietRecommendServices
from .serializer import dietRecommendServicesSerializer

# Create your views here.

class DietRecommendServicesListView(APIView):
    def get(self, request):
        diet_recommend_services = DietRecommendServices.objects.all()
        serializer = dietRecommendServicesSerializer(diet_recommend_services, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = dietRecommendServicesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'data': serializer.data,
                'message':'Success'
            }
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
