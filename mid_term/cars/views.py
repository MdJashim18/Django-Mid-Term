from django.shortcuts import render
from django.views.generic import ListView, DetailView,TemplateView
from .models import Car, Brand
from django.shortcuts import redirect
from django.views import View
from .models import Order, Car
from .import models,forms
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Create your views here.


@method_decorator(login_required, name='dispatch')
class DetailsPostView(DetailView):
    model = Car
    template_name = 'car_detail.html'

    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data=self.request.POST)
        post = self.get_object()  
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = post
            new_comment.save()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all()
        context['comment_form'] = forms.CommentForm()
        return context





class OrderHistoryView(View):
    def get(self, request):
        if request.user.is_authenticated:
            orders = Order.objects.filter(user=request.user)
            return render(request, 'order.html', {'orders': orders})
        return redirect('login')
    


class CreateOrderView(View):
    def post(self, request, pk):
        car = Car.objects.get(pk=pk)
        if request.user.is_authenticated and car.quantity > 0:
            Order.objects.create(user=request.user, car=car)
            car.quantity -= 1
            car.save()
            return redirect('order-history')
        return redirect('login')
