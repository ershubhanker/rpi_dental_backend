from django.shortcuts import render, get_object_or_404, redirect
from .models import Patient
from .forms import PatientForm
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PatientSerializer
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os

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


@csrf_exempt
def save_selected_patients(request):
    if request.method == "POST":
        try:
            # Parse JSON data
            data = json.loads(request.body)
            selected_patients = data.get("patients", [])
            if not selected_patients:
                return JsonResponse({"error": "No patients selected."}, status=400)

            # Define the path to save the file
            react_project_path = "F:/projects/Python/Kai gao project/react/dentalfront"
            file_path = os.path.join(react_project_path, "patient.json")

            # Save data to the JSON file
            with open(file_path, "w") as json_file:
                json.dump({"patients": selected_patients}, json_file, indent=2)

            return JsonResponse({"message": "Data saved successfully."}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format."}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request method."}, status=400)