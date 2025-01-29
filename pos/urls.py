# from django.urls import path
# from . import views 

# urlpatterns = [
#     path('',views.home)
# ]

from django.urls import path
from .views import home, place_order,render

urlpatterns = [
    path('', home, name='home'),
    path('order/', place_order, name='place_order'),
    path('order-success/', lambda request: render(request, 'order_success.html'), name='order_success'),
]

