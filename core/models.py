from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class Sex(models.TextChoices):
    MALE = "M", _("Male")
    FEMALE = "F", _("Female")
    PREFER_NOT_TO_SAY = "N", _("Prefer not to say")

class Doctor(AbstractUser):
    crm = models.CharField(max_length=20, blank=True, unique=False)
    specialty = models.CharField(max_length=100, blank=True)

class Patient(models.Model):
    first_name = models.CharField(max_length=250, blank=False)
    last_name = models.CharField(max_length=250, blank = False)
    birth_date = models.DateField()
    sex = models.CharField(
        max_length=1,
        choices=Sex.choices,
        default = Sex.PREFER_NOT_TO_SAY
    )
    phone = models.CharField(max_length=20, blank=True)
    notes = models.TextField(max_length=1000, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Consultation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="consultations",)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE,related_name="consultations",)
    raw_notes = models.TextField(max_length=1000, blank=False)
    ai_summary = models.TextField(max_length=1000, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
