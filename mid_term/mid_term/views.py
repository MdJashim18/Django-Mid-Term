from django.shortcuts import render
from cars.models import Car,Brand


def home(request):
    brand_name = request.GET.get('brand')  
    if brand_name:
        cars = Car.objects.filter(brand__name=brand_name) 
    else:
        cars = Car.objects.all()  
    brands = Brand.objects.all()  
    return render(request, 'home.html', {'cars': cars, 'brands': brands})