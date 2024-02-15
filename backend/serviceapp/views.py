from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import DietRecomSerializer
from .foodrecomd import FoodRecommendation

import joblib
import numpy as np
import pandas as pd
import re

class DietRecommendationView(APIView):
    def post(self, request):
        try:
            # Load the model
            model_path = 'serviceapp/PredictedModel/model.joblib'
            model = joblib.load(model_path)
            
            # Load the Dataset
            dataFilePath = 'serviceapp/data/data.csv'
            df = pd.read_csv(dataFilePath)
            
            # Process request data with serializer
            serializer = DietRecomSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            filtered_data = serializer.validated_data.copy()
            filtered_data.pop('id', None)
            filtered_data.pop('user', None)
            
            # Calculate calories
            obj = FoodRecommendation(**filtered_data)
            calories = obj.calories()
            
            # Predict calories for each meal and fetch recommended food items
            recommended_food_items = {}
            for meal in ['breakfast', 'lunch', 'snacks', 'dinner']:
                meal_calories = calories[meal]
                meal_prediction = model.predict(np.array(meal_calories).reshape(-1, 1))
                meal_df = df.loc[(df[meal.capitalize()] == 1) & (df['cluster'] == meal_prediction[0]), ['food_items', 'Calories']].sort_values(by='Calories').head()
                recommended_food_items[meal] = meal_df
                
            
            return Response({
                'recommended_food_items': recommended_food_items
            }, status=status.HTTP_200_OK)
        
        except Exception as e:
            error_messages = str(e)
            required_messages = {}
            for match in re.finditer(r"'(.*?)': \[ErrorDetail\(string='(.*?)', code='(.*?)'\)\]", error_messages):
                field, message = match.group(1), match.group(2)
                if field != 'unknown':  
                    required_messages[field] = message
            return Response({'error_messages': required_messages}, status=status.HTTP_400_BAD_REQUEST)
