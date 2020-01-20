""" Sponsorship serializers"""

from rest_framework import serializers

from src.api.models import Application, Sponsorship


class SponsorshipSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sponsorship
        fields = ('name', 'description')

        
class ApplicationSerializer(serializers.ModelSerializer):
    student = serializers.SerializerMethodField()
    sponsorship = serializers.SerializerMethodField()

    def get_student(self, obj):
        return obj.student.username

    def get_sponsorship(self, obj):
        return obj.sponsorship.name

    class Meta:
        model = Application
        fields = ('student', 'sponsorship')
