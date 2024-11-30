from django.shortcuts import render, get_object_or_404, redirect
from .models import Patient
from .forms import PatientForm
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PatientSerializer
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view

def index(request):
    return render(request, 'calendar.html')

# List all patients or create a new patient
@api_view(['GET', 'POST'])
def patient_list_create(request):
    if request.method == 'GET':
        patients = Patient.objects.all()
        # Serialization of data is required to convert data format compatible for API
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Retrieve, update, or delete a patient
@api_view(['GET', 'PUT', 'DELETE'])
def patient_detail(request, pk):
    try:
        patient = Patient.objects.get(pk=pk)
    except Patient.DoesNotExist:
        return Response({'error': 'Patient not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PatientSerializer(patient)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PatientSerializer(patient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        patient.delete()
        return Response({'message': 'Patient deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

# Function to make advance search 
@api_view(['GET'])
def patient_search(request):
    """
    Search patients by first name, last name, address, or phone number.
    """
    # Extract query parameters
    first_name = request.query_params.get('first_name', None)
    last_name = request.query_params.get('last_name', None)
    address = request.query_params.get('address', None)
    phone_number = request.query_params.get('phone_number', None)

    # Filter the queryset
    patients = Patient.objects.all()

    if first_name:
        patients = patients.filter(first_name__icontains=first_name)
    if last_name:
        patients = patients.filter(last_name__icontains=last_name)
    if address:
        patients = patients.filter(address__icontains=address)
    if phone_number:
        patients = patients.filter(phone_number__icontains=phone_number)

    # Serialize and return the data
    serializer = PatientSerializer(patients, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)