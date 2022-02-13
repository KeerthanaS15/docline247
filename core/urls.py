from django.conf.urls import handler500
from django.urls import path, re_path
from . import views
from .views import HomePageView, DoctorPageView

app_name = 'core'

urlpatterns = [
    path('', HomePageView.as_view(), name='home-page'),
    path('doctors/', DoctorPageView.as_view(), name='doctor-page'),
]
