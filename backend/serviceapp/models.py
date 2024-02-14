from django.db import models
from authapp.models import User

# Service Models.
class DietRecommendation(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    PHYSICAL_CHOICES = [
        ('1','Sedentray'),
        ('2','LightlyActive'),
        ('3','ModeratelyActive'),
        ('4','ExtremelyActive'),
    ]  
    GOAL_CHOICES = [
        ('1','Weight Loss'),
        ('2','Weight Gain'),
        ('3','Maintain Weight'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    weight = models.FloatField()
    height = models.FloatField()
    physical_activity = models.CharField(max_length = 1 ,choices=PHYSICAL_CHOICES)
    goal = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.user)
