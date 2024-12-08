from django.db import models

class Patient(models.Model):
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
        ('Discharged', 'Discharged'),
    ]

    patient_id = models.AutoField(primary_key=True)  # Auto-incrementing primary key
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Active', blank=True, null=True)

    def __str__(self):
        return f"{self.first_name or 'Unknown'} {self.last_name or ''}".strip()


class Meeting(models.Model):
    patient_details = models.ForeignKey(Patient, on_delete=models.CASCADE, blank=True,null=True)
    title = models.CharField(max_length=100, blank=True,null=True)
    doctor_name = models.CharField(max_length=100)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()

    def __str__(self):
        return f"{self.patient_details} with {self.doctor_name} on {self.start_datetime.strftime('%Y-%m-%d %H:%M')}"

    # class Meta:
    #     ordering = ['start_datetime']
    #     verbose_name = "Meeting"
    #     verbose_name_plural = "Meetings"