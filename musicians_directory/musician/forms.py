from django import forms 
from django.core import validators
from musician.models import MusicianModel



class MusicianForm(forms.ModelForm):
    class Meta:
        model = MusicianModel
        fields = '__all__'
        labels = {
            'first_name' : 'First Name',
            'last_name' : 'Last Name',
            'email' : 'Email',
            'phone' : 'Phone Number',
            'instrument_type' : 'Instrument Type',
        }