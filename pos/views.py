from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Coffee
from .forms import OrderForm
from django.contrib import messages
from .forms import SignUpForm

def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have successfully signed up!")
            return redirect('home')  # Redirect to the home page after successful signup
        else:
            messages.error(request, "There was an error with your form.")

    else:
        form = SignUpForm()

    return render(request, 'pos/login_signup.html', {'form': form})


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
