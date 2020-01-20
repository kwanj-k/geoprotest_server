""" Sponsorship model """

from django.db import models

from src.api.models.base import CommonFieldsMixin
from .user import User

class Sponsorship(CommonFieldsMixin):
    name = models.CharField(max_length=30, null=False, blank=False)
    description = models.CharField(max_length=30, null=False, blank=False)

    def __str__(self):
        return self.name

class Application(CommonFieldsMixin):
    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='applications'
    )
    sponsorship = models.ForeignKey(
        Sponsorship,
        on_delete=models.CASCADE,
        related_name='applications'
    )

    def __str__(self):
        return '{} {}'.format(self.student.username, self.sponsorship.name)
    
    class Meta:
        unique_together = ['student', 'sponsorship']
