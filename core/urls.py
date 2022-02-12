from django.conf.urls import handler500
from django.urls import path, re_path
from . import views
<<<<<<< HEAD
from .views import HomePageView, DoctorPageView
=======
from .views import HomePageView,DoctorPageView
>>>>>>> b5354de487e47012bcc273b194d7381182119dad

app_name = 'core'

urlpatterns = [
    path('', HomePageView.as_view(), name='home-page'),
<<<<<<< HEAD
    path('doctors', DoctorPageView.as_view(), name='doctor-page'),
=======
    path('doctors/', DoctorPageView.as_view(), name='doctor-page'),

>>>>>>> b5354de487e47012bcc273b194d7381182119dad
]
