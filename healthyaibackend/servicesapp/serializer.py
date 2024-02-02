from django.contrib.auth.models import User
from rest_framework import serializers
from .models import DietRecommendServices



class dietRecommendServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DietRecommendServices
        fields = ['id','age', 'weight', 'height', 'gender', 'physical_activity', 'goal']
   
    def validate(self,data):
        age = data.get('age')
        if age is not None and age < 0 :
            raise serializers.ValidationError('Age must be between 15 and 75')
        
        weight = data.get('weight')
        if weight is not None and weight<0:
            raise serializers.ValidationError("Weight must be  a postivite number")
        height = data.get('height')
        if height is not None and height < 0:
            raise serializers.ValidationError("Height must be a positive integer.")
        return data
        
    def save(self):
        dietRecommend = DietRecommendServices(age = self.validated_data['age'], weight=self.validated_data['weight'], height = self.validated_data['height'], gender = self.validated_data['gender'], physical_activity = self.validated_data['physical_activity'],goal = self.validated_data['goal'])
        dietRecommend.save()
        
        return dietRecommend      
        
