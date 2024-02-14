from django.urls import path
from .views import DietRecommendationView

urlpatterns = [
    path('dietrecommendation/',DietRecommendationView.as_view(),name='dietrecommendation'),
]