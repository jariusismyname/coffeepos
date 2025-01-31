from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Coffee
from .forms import OrderForm

def home(request):
    coffee = Coffee.objects.all()
    return render(request, 'home.html', {'coffee': coffee})

def login_signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)  # Ensure username == email
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'pos/login_signup.html', {'error': 'Invalid credentials'})
    return render(request, 'pos/login_signup.html')

def signup_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if password == confirm_password:
            user = User.objects.create_user(username=email, email=email, password=password)
            user.first_name = name
            user.save()
            return redirect('login')  # Ensure 'login' exists in urlpatterns
        else:
            return render(request, 'pos/login_signup.html', {'error': 'Passwords do not match'})
    return render(request, 'pos/login_signup.html')

def place_order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            coffee = get_object_or_404(Coffee, id=form.cleaned_data['coffee'].id)
            if coffee.stock >= form.cleaned_data['quantity']:
                order = form.save(commit=False)
                order.total_price = order.quantity * coffee.price
                order.save()
                coffee.stock -= order.quantity
                coffee.save()
                return redirect('order_success')
            else:
                return render(request, 'place_order.html', {'form': form, 'error': "Not enough stock!"})
    else:
        form = OrderForm()
    return render(request, 'place_order.html', {'form': form})

def order_success(request):
    return render(request, 'order_success.html')
