from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', views.register, name='signup'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/' , views.edit_profile,name='edit_profile'),
    path('profile/edit/pass_change/' , views.pass_change,name='pass_change'),
    path('logout/', LogoutView.as_view(next_page='homepage'), name='logout'),
]
