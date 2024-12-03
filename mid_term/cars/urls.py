from django.urls import path
from .views import DetailsPostView,OrderHistoryView,CreateOrderView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('detail/<int:pk>/', DetailsPostView.as_view(), name='car-detail'),
    path('order-history/', OrderHistoryView.as_view(), name='order-history'),
    path('car-buy/<int:pk>/', CreateOrderView.as_view(), name='car-buy'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
