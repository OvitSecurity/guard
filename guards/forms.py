from django import forms
from .models import Guard
from django.forms import ModelForm, Textarea, TextInput



class GuardForm(forms.ModelForm):
    class Meta:
        model = Guard
        fields = ('name', 'lastname', 'email', 'telephone', 'am', 'birthdate', 'fathersname', 'fatherslastname', 'mothersname' , 'motherslastname', 'marital', 'childs', 'address', 'identity', 'amka', 'ama', 'afm', 'license_issue_date', 'height', 'weight', 'shoe', 'gender')
        widgets = {
            'name': TextInput(attrs={'class': 'form-group'}),
        }