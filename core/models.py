from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError
from .utils import unique_slug_generator
from django.db.models.signals import pre_save
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):

    class Meta:
        db_table = 'dl_users'


class CategoryManager(models.Manager):

    def get_by_natural_key(self, name):
        return self.get(name=name)


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    icon = models.ImageField(upload_to='categories/')

    objects = CategoryManager()

    class Meta:
        db_table = 'dl_categories'

    def __str__(self) -> str:
        return self.name


class DoctorManager(models.Manager):

    def get_by_natural_key(self, name):
        return self.get(name=name)


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
    profile_pic = models.ImageField(upload_to='doctors/')

    objects = DoctorManager()

    class Meta:
        db_table = 'dl_doctors'

    def __str__(self) -> str:
        return self.name


class PatientManager(models.Manager):

    def get_by_natural_key(self, name):
        return self.get(name=name)


class Patient(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()
    dob = models.DateField()

    objects = PatientManager()

    class Meta:
        db_table = 'dl_patients'

    def __str__(self) -> str:
        return self.name


class Appointment(models.Model):

    class StatusChoices(models.TextChoices):
        IN_PROGRESS = 'IN PROGRESS', _('In Progress')
        ACCEPTED = 'ACCEPTED', _('Accepted')
        REJECTED = 'REJECTED', _('Rejected')
        CANCELED = 'CANCELED', _('Canceled')

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date_of_appointment = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    time_slot = models.TimeField()
    message = models.TextField()
    slug = models.SlugField(max_length=250, null=True, blank=True)
    status = models.CharField(max_length=11,
                              choices=StatusChoices.choices, default=StatusChoices.IN_PROGRESS)

    class Meta:
        db_table = 'dl_appointments'

    def save(self, *args, **kwargs):
        if(self.doctor.category != self.category):
            raise ValidationError("Doctor and Category do not match")
        super(Appointment, self).save(*args, **kwargs)
        # endif

    def __str__(self) -> str:
        return str(self.patient)


def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
        print(instance.slug)


pre_save.connect(pre_save_receiver, sender=Appointment)
