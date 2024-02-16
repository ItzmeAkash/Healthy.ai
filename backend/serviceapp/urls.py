from django.urls import path
from .views import DietRecommendationView,FoodClasssificationView

urlpatterns = [
    path('dietrecommendation/',DietRecommendationView.as_view(),name='dietrecommendation'),
    path('foodimageclassification/',FoodClasssificationView.as_view(),name='dietrecommendation'),
]