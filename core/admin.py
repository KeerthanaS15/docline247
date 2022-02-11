from django.contrib import admin
from .models import User, Category, Doctor, Patient, Appointment
# Register your models here.

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Appointment)
