from django.shortcuts import render
from django.views.generic import TemplateView, ListView, UpdateView
from .models import Category, Doctor, Patient, Appointment
from django.views.generic import FormView
from django.urls import reverse, reverse_lazy
from .forms import AppointmentCreateForm
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.html import strip_tags
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.contrib import messages


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
            messages.success(self.request, 'Form submitted successfully')

            # current_site = get_current_site(request)
            # subject = 'Appointment'
            # from_email = settings.EMAIL_HOST_USER
            # to = cd['email']
            # slug = Appointment.objects.get(
            #     id=appointment.id).slug
            # message = render_to_string(
            #     'core/email.html', {
            #         'name': cd['name'],
            #         'date_of_appointment': cd['date_of_appointment'],
            #         'domain': current_site,
            #         'slug': slug,
            #     }
            # )
            # text_content = strip_tags(message)
            # msg = EmailMultiAlternatives(
            #     subject, text_content, from_email, [to])
            # msg.attach_alternative(message, "text/html")
            # msg.send()

            return self.form_valid(appointment_form)

        else:
            return render(self.request, 'core/book-appointment.html', context)


class AppointmentDetailView(UpdateView):
    template_name = 'core/appointment-detail.html'
    model = Appointment
    context_object_name = 'appointment'
    fields = ['status']

    def get_success_url(self):
        return reverse('core:appointment_detail', kwargs={'slug': self.object.slug})
