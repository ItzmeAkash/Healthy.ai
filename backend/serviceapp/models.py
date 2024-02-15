from django.db import models
from authapp.models import User

# Service Models.
class DietRecommendation(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    PHYSICAL_CHOICES = [
        ('Sedentray','Sedentray'),
        ('LightlyActive','LightlyActive'),
        ('ModeratelyActive','ModeratelyActive'),
        ('ExtremelyActive','ExtremelyActive'),
    ]  
    GOAL_CHOICES = [
        ('WeightLoss','WeightLoss'),
        ('WeightGain','WeightGain'),
        ('MaintainWeight','MaintainWeight'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='dietRecommendations')
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    weight = models.FloatField()
    height = models.FloatField()
    physical_activity = models.CharField(max_length = 50 ,choices=PHYSICAL_CHOICES)
    goal = models.CharField(max_length=100,choices=GOAL_CHOICES)
    
    def __str__(self):
        return str(self.user)
