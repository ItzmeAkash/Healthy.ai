from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .serializer import DietRecomSerializer,FoodImageSerializer
from .foodrecomd import FoodRecommendation
from .models import FoodImageModel
from keras.models import load_model
from keras.preprocessing.image import load_img,img_to_array
import joblib
import numpy as np
import pandas as pd
import re
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO


# Diet Recommendation View
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


# Food Classification View
class FoodClassificationView(generics.CreateAPIView):
    queryset = FoodImageModel.objects.all()
    serializer_class = FoodImageSerializer

    def create(self, request):
        try:
            # Load the model
            model_path = 'serviceapp/PredictedModel/foodimagemodel.h5'
            model = load_model(model_path)
            
            # Get the image file from the request
            image_file = request.FILES.get('image')            
            if image_file:
                # Load and preprocess the image
                # Convert InMemoryUploadedFile to BytesIO
                image_file_data = BytesIO(image_file.read())
                image = load_img(image_file_data, target_size=(224, 224))
                image = img_to_array(image)
                image = np.expand_dims(image, axis=0)

                # Predict the class of the image
                result = np.argmax(model.predict(image), axis=1)
                print(result)
                
                #Load the Food Image Labels
                labels_path = 'serviceapp/data/foodimagelabels.txt'
                with open(labels_path, 'r') as file:
                    food_items = file.read().splitlines()
                    #Find the Food name according to the labels
                    predicted_food_items = food_items[result[0]-1] if 0 <= result[0] < len(food_items) else "Unknown" 
                # Save the result to the database or perform any other actions
                return Response({"status": "success", "predicted_class": int(result[0]),"foodname":predicted_food_items}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'No image provided'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(f"Error: {e}")
            return Response({'error': 'An error occurred while processing the image'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            