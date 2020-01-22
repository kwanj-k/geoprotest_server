""" Sponsorship serializers"""

from rest_framework import serializers

from src.api.models import Application, Sponsorship


class SponsorshipSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sponsorship
        fields = ('name', 'description', 'pk')

        
class ApplicationSerializer(serializers.ModelSerializer):
    student = serializers.SerializerMethodField()
    sponsorship = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()
    
    def get_email(self, obj):
        return obj.student.email

    def get_student(self, obj):
        return obj.student.username

    def get_sponsorship(self, obj):
        return obj.sponsorship.description

    class Meta:
        model = Application
        fields = (
            'student', 'sponsorship', 'first_name', 'last_name', 'mobile', 'country',
            'city', 'school_name', 'degree', 'cover_letter', 'start', 'to', 'postal_code',
            'birth_certificate', 'national_id', 'is_approved', 'is_rejected', 'pk', 'email'
        )
