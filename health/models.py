from django.db import models

# Create your models here.
class Department(models.Model):
    department_name=models.CharField(max_length=150)
    department_description=models.TextField()
    department_image = models.ImageField(upload_to='department/')

    def __str__(self):
        return self.department_name


class DoctorDetail(models.Model):
    department_name = models.ForeignKey(Department,on_delete=models.CASCADE)
    doctor_full_name=models.CharField(max_length=150)
    gender=models.CharField(max_length=10)
    age=models.SmallIntegerField()
    education_status=models.CharField(max_length=150)
    work_experience=models.SmallIntegerField()
    email = models.EmailField()
    mobile_number = models.CharField(max_length=15)
    doctor_description=models.TextField()
    available_work_hours=models.SmallIntegerField()
    state=models.CharField(max_length=100) 
    city=models.CharField(max_length=100)
    doctor_image = models.ImageField(upload_to='doctor/')

    def __str__(self):
        return self.doctor_full_name
    
class AppointmentDetails(models.Model):
    doctor_name=models.CharField(max_length=150)
    patient_name=models.CharField(max_length=150)
    patient_email=models.EmailField()
    patient_mobile_number=models.CharField(max_length=15)
    appointment_date=models.DateField()
    appointment_time=models.TimeField()
    prescription = models.ImageField(upload_to='prescription/', null=True, blank=True)
    message = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Appointment for {self.patient_name} with Dr. {self.doctor_name} on {self.appointment_date} at {self.appointment_time}"
    
class Queries(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    subject=models.CharField(max_length=200)
    phone=models.CharField(max_length=15)
    message=models.TextField()

    def __str__(self):
        return f"{self.name} - {self.subject}"