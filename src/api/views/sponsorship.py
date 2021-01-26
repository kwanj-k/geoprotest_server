""" Sponsorship views"""
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.generics import (
    ListCreateAPIView,
    CreateAPIView,
    ListAPIView
)
from src.api.serializers.sponsorship import SponsorshipSerializer, ApplicationSerializer
from src.api.models import Sponsorship, Application


class SponsorshipViewSet(viewsets.ModelViewSet):
    serializer_class = SponsorshipSerializer
    queryset = Sponsorship.objects.all()


class ApplicationCreateAPIView(CreateAPIView):
    """ Create applications """
    serializer_class = ApplicationSerializer
    queryset = Application.objects.all()

    def create(self, request, *args, **kwargs):
        """ Apply for a sponorship"""
        sponsorship_id = kwargs['sponsorship_id']
        sponsorship = Sponsorship.objects.get(pk=sponsorship_id)
        if not sponsorship:
            message = {"error": "Sponsorship does not exist."}
            return Response(message, status.HTTP_404_NOT_FOUND)
        try:
            application_exists = Application.objects.get(
                student=request.user,
                sponsorship=sponsorship
            )
        except:
            application_exists = None
        if application_exists:
            message = {"error": "Application already sent."}
            return Response(message, status.HTTP_400_BAD_REQUEST)
        context = {
            'request': request,
            'student': request.user,
            'sponsorship': sponsorship
        }
        serializer = self.serializer_class(data=request.data, context=context)
        serializer.is_valid(raise_exception=True)
        serializer.save(student=request.user, sponsorship=sponsorship)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ApplicationListAPIView(ListAPIView):
    """ List applications """
    serializer_class = ApplicationSerializer
    queryset = Application.objects.all()
