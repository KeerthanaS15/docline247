from pydoc import Doc
from re import template
from unicodedata import category
from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView, ListView
from .models import Doctor
from django.core.paginator import Paginator
# Create your views here.


class HomePageView(TemplateView):

    template_name = "core/home.html"

<<<<<<< HEAD

class DoctorPageView(ListView):

    template_name = 'core/doctors.html'
    paginate_by = 2
    model = Doctor
    ordering = 'id'
    context_object_name = 'all_doctors_details'

    def get_queryset(self):
        queryset = self.model.objects.all()
        if(self.request.GET.get('category')):
            queryset = Doctor.objects.filter(category__name=self.request.GET.get('category'))
        return queryset


=======
class DoctorPageView(TemplateView):

    template_name = "core/doctor.html"
>>>>>>> b5354de487e47012bcc273b194d7381182119dad
