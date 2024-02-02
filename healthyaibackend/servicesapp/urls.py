from django.urls import path
from .views import DietRecommendServicesListView

urlpatterns = [
    path('dietrecommendservices/', DietRecommendServicesListView.as_view()),
    
]
