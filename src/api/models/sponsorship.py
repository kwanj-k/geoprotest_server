""" Sponsorship model """
import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _

from phone_field import PhoneField

from src.api.models.base import CommonFieldsMixin
from .user import User


def from_year_choices():
    return [(r,r) for r in range(2002, datetime.date.today().year+1)]

def to_year_choices():
    return [(r,r) for r in range(datetime.date.today().year, datetime.date.today().year+10)]

def current_year():
    return datetime.date.today().year

class Sponsorship(CommonFieldsMixin):
    name = models.CharField(max_length=30, null=False, blank=False)
    description = models.CharField(max_length=300, null=False, blank=False)

    def __str__(self):
        return self.name

class Application(CommonFieldsMixin):
    is_approved= models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)
    first_name = models.CharField(max_length=30, null=False, blank=False)
    last_name = models.CharField(max_length=30, null=False, blank=False)
    mobile  = PhoneField(blank=True, help_text='Contact phone number')
    country = models.CharField(max_length=30, null=False, blank=False)
    city = models.CharField(max_length=30, null=False, blank=False)
    school_name = models.CharField(max_length=50, null=False, blank=False)
    degree = models.CharField(max_length=100, null=False, blank=False)
    cover_letter = models.CharField(max_length=1000, null=False, blank=False)
    start = models.IntegerField(
        _('start'), 
        choices=from_year_choices(), 
        default=current_year())
    to = models.IntegerField(
        _('to'), 
        choices=to_year_choices(), 
        default=current_year())
    postal_code = models.CharField(
        "ZIP / Postal code",
        max_length=12,
    )
    birth_certificate = models.URLField(
        blank=True,
        null=True,
        default="https://res.cloudinary.com/dakhp08gq/image/upload/v1579606701/noimage.png"
    )
    national_id = models.URLField(
        blank=True,
        null=True,
        default="https://res.cloudinary.com/dakhp08gq/image/upload/v1579606701/noimage.png"
    )
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
