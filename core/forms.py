from datetime import datetime, date, timedelta
from django import forms
from .models import Doctor, Category
from django.core.validators import MinLengthValidator


def dob(value):
    if value > date.today():
        raise forms.ValidationError("Date of birth cannot be a future date")


def date_of_appointment(value):
    if value < date.today():
        raise forms.ValidationError(
            "Please add future date")


class AppointmentCreateForm(forms.Form):
    name = forms.CharField(max_length=128, validators=[MinLengthValidator(5)], widget=forms.TextInput(attrs={
        'class': 'm-form__input m-form__input--name',
        'placeholder': 'Name'
    }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'm-form__input m-form__input--email',
        'placeholder': 'Email'

    }))

    dob = forms.DateField(validators=[dob], widget=forms.DateInput(attrs={
        'class': 'm-form__input m-form__input--dob',
        'placeholder': 'Date of birth'

    }))

    date_of_appointment = forms.DateField(validators=[date_of_appointment], widget=forms.DateInput(attrs={
        'class': 'm-form__input m-form__input--doa',
        'placeholder': 'Date of appointment'
    }))

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(), widget=forms.Select(attrs={
            'class': 'm-form__input m-form__input--designation',
        }))

    doctor = forms.ModelChoiceField(queryset=Doctor.objects.all(), widget=forms.Select(attrs={
        'class': 'm-form__input m-form__input--doctor',
    }))

    time_slot = forms.TimeField(widget=forms.TimeInput(attrs={
        'class': 'm-form__input m-form__input--time',
        'placeholder': 'Time slot'
    }))

    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'm-form__input m-form__input--notes',
        'placeholder': 'Convey details to doctor'
    }))

    def __init__(self, *args, **kwargs):
        super(AppointmentCreateForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = ""
        self.fields['email'].label = ""
        self.fields['dob'].label = ""
        self.fields['category'].empty_label = "Select a category"
        self.fields['doctor'].empty_label = "Select a doctor"
        self.fields['date_of_appointment'].label = ""
        self.fields['category'].label = ""
        self.fields['doctor'].label = ""
        self.fields['time_slot'].label = ""
        self.fields['message'].label = ""

    def clean(self):
        cleaned_data = super().clean()
        date_of_appointment = cleaned_data.get('date_of_appointment')
        time_slot = cleaned_data.get('time_slot')
        if(date_of_appointment == date.today()):
            if(time_slot <= datetime.now().time()):
                raise forms.ValidationError("Please enter valid time-slot")
