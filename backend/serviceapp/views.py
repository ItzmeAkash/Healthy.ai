from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . serializer import DietRecomSerializer

# Create View for DietRecommendation
def DietRecommendationView(APIView):
    def post(self,request):
        serializer = DietRecomSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            user.save()
            print(user)
            return Response({
                'message': 'Breakfast'
            })    
        
        return Response({'message' :'error'})
        
   