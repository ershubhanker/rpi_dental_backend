from rest_framework import serializers
from .models import Patient, Meeting


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'  # Include all fields in the API

class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = ['id', 'patient_details','title', 'doctor_name', 'start_datetime', 'end_datetime']

    def validate(self, data):
        # Example: Ensure start time is before end time
        if data['start_datetime'] >= data['end_datetime']:
            raise serializers.ValidationError("Start time must be before end time.")
        return data
