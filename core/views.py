from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Category, Doctor, Patient, Appointment
from django.views.generic import FormView
from django.urls import reverse_lazy
from .forms import AppointmentCreateForm


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
            queryset = Doctor.objects.filter(
                category__name=self.request.GET.get('category'))
        # endif

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        get_copy = self.request.GET.copy()
        parameters = get_copy.pop('page', True) and get_copy.urlencode()
        context['parameters'] = parameters
        return context


class BookAppointment(FormView):
    template_name = 'core/book-appointment.html'
    form_class = AppointmentCreateForm
    success_url = reverse_lazy('core:book-appointment')

    def post(self, request, *args, **kwargs):
        appointment_form = AppointmentCreateForm(request.POST)
        context = super(BookAppointment, self).get_context_data(**kwargs)
        if appointment_form.is_valid():
            cd = appointment_form.cleaned_data
            patient, created = Patient.objects.get_or_create(
                name=cd['name'], email=cd['email'], dob=cd['dob'])
            appointment = Appointment(
                patient_id=patient.id,
                date_of_appointment=cd['date_of_appointment'],
                category=cd['category'],
                doctor=cd['doctor'],
                time_slot=cd['time_slot'],
                message=cd['message']
            )
            appointment.save()

            return self.form_valid(appointment_form)

        else:
            return render(self.request, 'core/book-appointment.html', context)
