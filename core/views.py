from django.shortcuts import render

from rest_framework import viewsets
from .models import Patient, Consultation
from .serializers import PatientSerializer, ConsultationSerializer


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class ConsultationViewSet(viewsets.ModelViewSet):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer