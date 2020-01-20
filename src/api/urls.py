from django.urls import path

from .views import *

urlpatterns = [
    path('register/', RegistrationAPIView.as_view(), name='register'),
    path('login/', LoginGenericAPIView.as_view(), name='login'),
    path('sponsorship/', SponsorshipListCreateAPIView.as_view(), name='sponsorship'),
    path('apply/<int:sponsorship_id>/', ApplicationCreateAPIView.as_view(), name='apply'),
    path('applications/', ApplicationListAPIView.as_view(), name='applications'),
]
