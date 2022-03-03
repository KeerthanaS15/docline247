from django import forms
from datetime import datetime, date
from .models import Doctor, Category
from django.core.validators import MinLengthValidator
from .validators import past_date_validator, future_date_validator, name_validator


class AppointmentCreateForm(forms.Form):

    time_choices = (
        ('09:00:00', '09:00 AM'),
        ('10:30:00', '10:30 AM'),
        ('12:00:00', '12:00 PM'),
        ('16:00:00', '04:00 PM'),
        ('18:00:00', '06:00 PM'),
    )

    name = forms.CharField(max_length=128,
                           validators=[MinLengthValidator(3), name_validator],
                           widget=forms.TextInput(attrs={
                               'class': 'm-form__input m-form__input--name',
                               'placeholder': 'Name'
                           }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'm-form__input m-form__input--email',
        'placeholder': 'Email'
    }))

    dob = forms.DateField(validators=[past_date_validator],
                          widget=forms.DateInput(attrs={
                              'class': 'm-form__input m-form__input--dob',
                              'placeholder': 'Date of birth',
                              'type': 'date'
                          }))

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={
            'class': 'm-form__input m-form__input--designation',
        }))

    doctor = forms.ModelChoiceField(queryset=Doctor.objects.all(),
                                    widget=forms.Select(attrs={
                                        'class': 'm-form__input m-form__input--doctor',
                                    }))

    date_of_appointment = forms.DateField(validators=[future_date_validator],
                                          widget=forms.DateInput(attrs={
                                              'class': 'm-form__input m-form__input--doa',
                                              'placeholder': 'Date of appointment',
                                              'type': 'date'
                                          }))

    time_slot = forms.ChoiceField(choices=time_choices,
                                  widget=forms.Select(attrs={
                                      'class': 'm-form__input m-form__input--time',
                                  }))

    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'm-form__input m-form__input--notes',
        'placeholder': 'Convey details to doctor'
    }))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
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
            if(time_slot <= str(datetime.now().time())):
                raise forms.ValidationError("Please select future time-slot")
            # endif
        # endif
