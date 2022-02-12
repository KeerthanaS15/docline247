# from django.db import models

# Create your models here.
from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError


class User(AbstractUser):

    class Meta:
        db_table = 'dl_users'


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = 'dl_categories'

    def __str__(self) -> str:
        return self.name


class Doctor(models.Model):

    class Gender(models.TextChoices):
        M = 'M'
        F = 'F'
        T = 'T'

    YEAR_CHOICES = []
    for year in range(1980, datetime.now().year+1):
        YEAR_CHOICES.append((year, year))

    name = models.CharField(max_length=128, unique=True)
    gender = models.CharField(max_length=1, choices=Gender.choices)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    age = models.PositiveSmallIntegerField()
    year_of_employment = models.IntegerField(choices=YEAR_CHOICES)

    class Meta:
        db_table = 'dl_doctors'

    def __str__(self) -> str:
        return self.name


class Patient(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()
    dob = models.DateField()

    class Meta:
        db_table = 'dl_patients'

    def __str__(self) -> str:
        return self.name


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date_of_appointment = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    time_slot = models.TimeField()
    message = models.TextField()

    class Meta:
        db_table = 'dl_appointments'

    def save(self, *args, **kwargs):
        if(self.doctor.category != self.category):
            raise ValidationError("Doctor and Category do not match")
        super(Appointment, self).save(*args, **kwargs)
        # endif

    def __str__(self) -> str:
        return str(self.patient)
