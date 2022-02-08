# from django.db import models

# Create your models here.
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
    name = models.CharField(max_length=128, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

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
        if(self.doctor.category == self.category):
            super(Appointment, self).save(*args, **kwargs)
        else:
            raise ValidationError("Doctor and Category do not match")
        # endif

    def __str__(self) -> str:
        return str(self.patient)
