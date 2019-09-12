from rest_framework import serializers
from medicalRecord.models import PatientForm


class PatientFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientForm
        fields = '__all__'