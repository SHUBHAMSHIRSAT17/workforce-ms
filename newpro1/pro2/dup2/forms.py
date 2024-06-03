from django import forms
from . models import Employee_model


class Employee_form(forms.ModelForm):
    class Meta:
        model = Employee_model
        fields = "__all__"