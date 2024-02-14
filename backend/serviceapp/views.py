from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . serializer import DietRecomSerializer
from . foodrecomd import FoodRecommendation
import re

# Create View for DietRecommendation
class DietRecommendationView(APIView):
    def post(self, request):
        try:  
            serializer = DietRecomSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                user = serializer.save()
                filtered_data = serializer.validated_data.copy()
                filtered_data.pop('id', None)
                filtered_data.pop('user', None)

                obj = FoodRecommendation(**filtered_data)
                calories = obj.calories()

                return Response({
                    'message': 'Calories calculated successfully',
                    'calories': calories
                }, status=status.HTTP_200_OK)
        
        except Exception as e:
            error_messages = str(e)
            required_messages = {}

            # Error message filtering
            for match in re.finditer(r"'(.*?)': \[ErrorDetail\(string='(.*?)', code='(.*?)'\)\]", error_messages):
                field, message = match.group(1), match.group(2)
                if field != 'unknown':  
                    required_messages[field] = message

            return Response({'error_messages': required_messages}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
