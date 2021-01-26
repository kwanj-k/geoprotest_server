from django.urls import path, include

from .views import *

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'sponsorship', SponsorshipViewSet, basename='sponsorship')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegistrationAPIView.as_view(), name='register'),
    path('login/', LoginGenericAPIView.as_view(), name='login'),
    path('apply/<int:sponsorship_id>/', ApplicationCreateAPIView.as_view(), name='apply'),
    path('applications/', ApplicationListAPIView.as_view(), name='applications'),
]
