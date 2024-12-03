from django import forms 
from django.core import validators
from album.models import AlbumModel



class AlbumForm(forms.ModelForm):
    class Meta:
        model = AlbumModel
        fields = '__all__'