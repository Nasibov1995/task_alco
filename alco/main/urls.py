from django.urls import path
from main.api.views import UserExtractionAPIView,BlockIPApi,UserListAPIView

urlpatterns = [
    
    # GET users
    path("",UserListAPIView.as_view()),
    
    # GET /download-users/?user_ids=2   -   Specific user's information
    # GET /download-users/                  -   All user's information
    path('download-users/', UserExtractionAPIView.as_view()),
    
    
    path('block/', BlockIPApi.as_view()),

]