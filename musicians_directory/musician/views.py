from django.shortcuts import render,redirect
from .forms import MusicianForm
from .import models,forms
from .forms import MusicianForm
from .models import MusicianModel
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator




#Class Based Views
class AddMusicians(CreateView):
    model = models.MusicianModel
    form_class = forms.MusicianForm
    template_name = 'musician.html'
    success_url = reverse_lazy('Musicians')

class Edit_musicians(UpdateView):
    model = models.MusicianModel
    form_class = forms.MusicianForm
    template_name = 'musician.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('Edit_musicians')


def delete_musicians(request,id):
    Musician = models.MusicianModel.objects.get(pk=id)
    Musician.delete()
    return redirect('Musicians')