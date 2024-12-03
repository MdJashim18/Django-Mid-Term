from django.shortcuts import render, redirect, get_object_or_404
from album.forms import AlbumForm
from album.models import AlbumModel 
from .import models
from .import forms
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator




class AddAlbum(CreateView):
    model = models.AlbumModel
    form_class = forms.AlbumForm
    template_name = 'album.html'
    success_url = reverse_lazy('homepage')





class Edit_Album(UpdateView):
    model = models.AlbumModel
    form_class = forms.AlbumForm
    template_name = 'album.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('homepage')





class Delete_Album(DeleteView):
    model = models.AlbumModel
    # form_class = forms.AlbumForm
    template_name = 'delete.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('homepage')
