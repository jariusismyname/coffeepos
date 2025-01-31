# from django.urls import path
# from . import views 

# urlpatterns = [
#     path('',views.home)
# ]

from django.urls import path
from .views import home, place_order,render,order_success

# urlpatterns = [
#     path('', home, name='home'),
#     path('order/', place_order, name='place_order'),
#     path('order-success/', lambda request: render(request, 'order_success.html'), name='order_success'),
# ]
# from django.urls import path
# from .views import place_order, home

urlpatterns = [
    path('', home, name='home'),
    path('place-order/', place_order, name='place_order'),
    path('order-success/', order_success, name='order_success'),  # Ensure this exists
]

