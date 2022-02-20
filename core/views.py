from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Category, Doctor, Patient
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import AppointmentCreateForm, PatientCreateForm


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


class BookAppointment(CreateView):

    model = Doctor
    template_name = 'core/book-appointment.html'
    form_class = AppointmentCreateForm
    success_url = reverse_lazy('core:book-appointment')

    def get_context_data(self, **kwargs):
        context = super(BookAppointment, self).get_context_data(**kwargs)

        if self.request.method == 'POST':
            patient_form = PatientCreateForm(
                self.request.POST, prefix='patient')
        else:
            patient_form = PatientCreateForm(prefix='patient')
        context['patient_form'] = patient_form
        # endif

        return context

    def post(self, request, *args, **kwargs):
        appointment_form = AppointmentCreateForm(request.POST)
        patient_form = PatientCreateForm(request.POST, prefix='patient')

        if appointment_form.is_valid() and patient_form.is_valid():
            patient, created = Patient.objects.get_or_create(
                name=patient_form.cleaned_data['name'], email=patient_form.cleaned_data['email'], dob=patient_form.cleaned_data['dob'])
            appointment = appointment_form.save(commit=False)
            appointment.patient_id = patient.id
            appointment.save()

            return self.form_valid(appointment_form)

        else:
            return render(self.request, 'form.html', 'Something went wrong')
        # endif
