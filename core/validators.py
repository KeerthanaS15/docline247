from datetime import date
from django import forms
from django.core.validators import RegexValidator


def past_date_validator(value: date):
    if value > date.today():
        raise forms.ValidationError("Date of birth cannot be a future date")


def future_date_validator(value: date):
    if value < date.today():
        raise forms.ValidationError(
            "Please add future date")


name_validator = RegexValidator(
    r'^[a-zA-Z]+[\']*$', 'Only alphabets are allowed.')
