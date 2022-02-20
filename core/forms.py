from django import forms
from .models import Appointment, Patient


class PatientCreateForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('name', 'email', 'dob')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'm-form__input m-form__input--name',
                'placeholder': 'Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'm-form__input m-form__input--email',
                'placeholder': 'Email'

            }),
            'dob': forms.DateInput(attrs={
                'class': 'm-form__input m-form__input--dob',
                'placeholder': 'Date of birth'

            })
        }

    def __init__(self, *args, **kwargs):
        super(PatientCreateForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = ""
        self.fields['email'].label = ""
        self.fields['dob'].label = ""


class AppointmentCreateForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('date_of_appointment',
                  'category', 'doctor', 'time_slot', 'message')
        widgets = {
            'date_of_appointment': forms.DateInput(attrs={
                'class': 'm-form__input m-form__input--doa',
                'placeholder': 'Date of appointment'
            }),
            'category': forms.Select(attrs={
                'class': 'm-form__input m-form__input--designation',
            }),
            'doctor': forms.Select(attrs={
                'class': 'm-form__input m-form__input--doctor',
            }),
            'time_slot': forms.TimeInput(attrs={
                'class': 'm-form__input m-form__input--time',
                'placeholder': 'Time slot'
            }),
            'message': forms.Textarea(attrs={
                'class': 'm-form__input m-form__input--notes',
                'placeholder': 'Convey details to doctor'
            })
        }

    def __init__(self, *args, **kwargs):
        super(AppointmentCreateForm, self).__init__(*args, **kwargs)
        self.fields['date_of_appointment'].label = ""
        self.fields['category'].label = ""
        self.fields['doctor'].label = ""
        self.fields['time_slot'].label = ""
        self.fields['message'].label = ""
