from django.db import models
from django.contrib.auth.models import AbstractUser
from .data import MEDICAL_DEPARTMENT
from .managers import CustomUserManager

# Base User model with common fields
class CustomUser(AbstractUser):
    # Add any common fields for all users here
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    home_address = models.TextField(blank=True, null=True)
    phone_number = models.PositiveIntegerField(blank=True, null=True)
    email = models.EmailField(max_length=254, unique=True)
    username = models.CharField(max_length=50, blank=True, null=True)

    # if is_expert is False, then the user is a patient
    is_expert = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Patient(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class NextOfKin(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)

    name = models.CharField(max_length=150)
    phone_number = models.PositiveIntegerField()
    address = models.TextField()
    relationship = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.name} is {self.patient.user.username}"

class PatientPreviousHospitalDetails(models.Model):
    name = models.CharField(max_length=150)
    address = models.TextField()
    phone_number = models.PositiveIntegerField()
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)



class Expert(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    hospital = models.ForeignKey('Hospital', on_delete=models.PROTECT)

HOSPITAL_TYPES = (
    ('PRIVATE', 'Private'),
    ('PUBLIC', 'Public'),
)
class Hospital(models.Model):
    name = models.CharField(max_length=150)
    contact = models.TextField()
    type = models.CharField(choices=HOSPITAL_TYPES, max_length=10)
    mission_statement = models.TextField()

    ministry_of_health_certificate = models.FileField(upload_to=f'{name}/ministry_of_health_certificate')
    hospital_photo = models.FileField(upload_to=f'{name}hospital_photo')
    business_certificate = models.FileField(upload_to=f'{name}/business_certificate')

    owners_name = models.CharField(max_length=150)
    owners_phone_number = models.PositiveIntegerField()

AGE_CATEGORY = (
    ('ADULT', 'Adult'),
    ('TEEN', 'Teen'),
    ('Child', 'Child')
)
class ExpertHospitalDetails(models.Model):
    medical_department = models.CharField(choices=MEDICAL_DEPARTMENT, max_length=150)
    age_category_expert_treat = models.CharField(choices=AGE_CATEGORY, max_length=10)
    expert = models.OneToOneField(Expert, on_delete=models.CASCADE)