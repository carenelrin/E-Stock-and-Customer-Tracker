# forms.py
from django import forms
from .models import Clients, Products, Services
from datetime import date

class ClientForm(forms.ModelForm):
    class Meta:
        model = Clients
        fields = ['client_id', 'first_name', 'last_name', 'phone_no', 'email_id', 'address']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['job_id', 'prod_name', 'category', 'brand', 'model', 'description']

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Services
        fields = ['service_id', 'priority', 'status', 'due_date']

    def clean_due_date(self):
        due_date = self.cleaned_data.get('due_date')
        if due_date and due_date <= date.today():
            raise forms.ValidationError('Due date must be in the future.')
        return due_date
