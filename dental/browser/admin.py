from django.contrib import admin
from .models import *


class PatientAdmin(admin.ModelAdmin):
  list_display = ("patient_id","first_name", "last_name", "status",)
  
admin.site.register(Patient, PatientAdmin)
