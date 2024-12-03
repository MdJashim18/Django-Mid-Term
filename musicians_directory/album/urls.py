from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.AddAlbum.as_view(), name='Album'),
    path('edit/<int:id>/', views.Edit_Album.as_view(), name='Edit_Album'),
    path('delete/<int:id>/', views.Delete_Album.as_view(), name='delete_album'),  
]
