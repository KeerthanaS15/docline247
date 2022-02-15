from pydoc import Doc
from re import template
from unicodedata import category
from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView, ListView
from .models import Category, Doctor
from django.core.paginator import Paginator
# Create your views here.


class HomePageView(TemplateView):

    template_name = "core/home.html"


class DoctorPageView(ListView):

    template_name = 'core/doctor.html'
    paginate_by = 2
    model = Doctor
    ordering = 'id'
    context_object_name = 'doctors'

    def get_queryset(self):
        queryset = self.model.objects.all()
        if(self.request.GET.get('category')):
            queryset = Doctor.objects.filter(category__name=self.request.GET.get('category'))
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class BookAppointment(TemplateView):

    template_name = "core/book-appointment.html"

