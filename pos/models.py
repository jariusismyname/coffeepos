# from django.db import models

# # Create your models here.
# class Coffee(models.Model):
#     name=models.CharField(max_length=255)
#     price=models.FloatField()
#     quantity=   models.IntegerField()
#     image=models.CharField(max_length=2083)

from django.db import models

class Coffee(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    quantity = models.IntegerField()
    image = models.CharField(max_length=2083)

# class Order(models.Model):
#     coffee = models.ForeignKey(Coffee, on_delete=models.CASCADE)  # Connects to Coffee
#     customer_name = models.CharField(max_length=255)
#     email = models.EmailField()
#     address = models.TextField()
#     quantity = models.PositiveIntegerField()
#     total_price = models.FloatField()
#     order_date = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Order {self.id} - {self.customer_name}"
class Order(models.Model):
    coffee = models.ForeignKey(Coffee, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.TextField()
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"Order for {self.customer_name} - {self.coffee.name}"
