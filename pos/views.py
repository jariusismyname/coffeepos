# from django.shortcuts import render
# from .models import Coffee

# def home(request):
#     coffee=Coffee.objects.all()
#     return render(request,'home.html',{'coffee':coffee})


from django.shortcuts import render, redirect
from .models import Coffee, Order
from .forms import OrderForm

def home(request):
    coffee = Coffee.objects.all()
    return render(request, 'home.html', {'coffee': coffee})

def place_order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.total_price = order.quantity * order.coffee.price  # Calculate total cost
            order.save()
            return redirect('order_success')  # Redirect to success page
    else:
        form = OrderForm()

    return render(request, 'place_order.html', {'form': form})

# from django.http import HttpResponse

# def home(request):
#     return HttpResponse('''
#         <!DOCTYPE html>
#         <html lang="en">
#         <head>
#             <meta charset="UTF-8">
#             <meta name="viewport" content="width=device-width, initial-scale=1.0">
#             <title>Home Page</title>
#             <style>
#                 body {
#                     font-family: Arial, sans-serif;
#                     margin: 0;
#                     padding: 0;
#                     background-color: #f9f9f9;
#                     color: #333;
#                 }
#                 .container {
#                     padding: 20px;
#                     text-align: center;
#                 }
#                 h1 {
#                     font-size: 2.5rem;
#                     color: #4CAF50;
#                 }
#                 h2 {
#                     font-size: 2rem;
#                     color: #555;
#                     margin-top: 20px;
#                 }
#                 .best-seller {
#                     margin-top: 30px;
#                     padding: 15px;
#                     background-color: #fff;
#                     border: 1px solid #ddd;
#                     border-radius: 8px;
#                     box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
#                     display: inline-block;
#                     max-width: 300px;
#                 }
#             </style>
#         </head>
#         <body>
#             <div class="container">
#                 <h1>Home Page</h1>
#                 <h2>Best Seller</h2>
#                 <div class="best-seller">
#                     <p><strong>Product Name:</strong> Coffee Mug</p>
#                     <p><strong>Price:</strong> $15</p>
#                     <p><strong>Rating:</strong> ⭐⭐⭐⭐⭐</p>
#                 </div>
#             </div>
#         </body>
#         </html>
#     ''')
