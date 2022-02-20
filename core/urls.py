from django.urls import path
from .views import HomePageView, DoctorPageView, BookAppointment

app_name = 'core'

urlpatterns = [
    path('', HomePageView.as_view(), name='home-page'),
    path('doctors/', DoctorPageView.as_view(), name='doctor-page'),
    path('book-appointment/', BookAppointment.as_view(), name='book-appointment'),
]
