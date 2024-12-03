from django.shortcuts import render
from musician.models import MusicianModel


def home(request):
    data = MusicianModel.objects.all()
    return render(request,'home.html' ,{'data' : data})