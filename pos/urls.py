from django.urls import path
from .views import home, place_order, login_signup , order_success  # Import only what's needed

urlpatterns = [
    
    path('', home, name='home'),
    path('place_order/', place_order, name='place_order'),
    path('pos/login_signup/', login_signup , name='login_signup'),
    path('order_success/', order_success, name='order_success'),  # Ensure order_success is defined in views.py
]
