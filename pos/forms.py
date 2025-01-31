from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name', 'email', 'address', 'coffee', 'quantity']
        widgets = {
            'coffee': forms.HiddenInput(),  # Hide coffee field
            'address': forms.Textarea(attrs={'rows': 3}),
            'quantity': forms.NumberInput(attrs={'min': 1}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Bootstrap classes to visible fields
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'