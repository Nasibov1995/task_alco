from django.urls import path
from main.api.views import UserExtractionAPIView,BlockIPApi

urlpatterns = [
    
    
    # GET /download-users/?user_ids=1,2,3   -   Specific user's information
    # GET /download-users/                  -   All user's information
    path('download-users/', UserExtractionAPIView.as_view()),
    
    
    path('block/', BlockIPApi.as_view()),

]