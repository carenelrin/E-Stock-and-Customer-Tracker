from django import forms
from .models import Clients, Products, Services, PostServices
from datetime import date

class CombinedForm(forms.Form):
    # Clients Section
    client_id = forms.IntegerField(required=True, label='Client ID')
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    phone_no = forms.CharField(max_length=20, required=True)
    email_id = forms.EmailField(required=False)
    address = forms.CharField(max_length=1000, required=True)

    # Products Section
    job_id = forms.CharField(required=True, label='Job ID')
    prod_name = forms.CharField(max_length=255, required=True)
    category = forms.ChoiceField(choices=Products.CATEGORY_CHOICES, required=True)
    brand = forms.CharField(max_length=255, required=True)
    model = forms.CharField(max_length=255, required=True)
    description = forms.CharField(max_length=1000, required=True)

    # Services Section
    service_id = forms.IntegerField(required=True, label='Service ID')
    priority = forms.ChoiceField(choices=Services.PRIORITY_CHOICES, required=True)
    status = forms.ChoiceField(choices=Services.STATUS_CHOICES, required=True)
    due_date = forms.DateField(widget=forms.SelectDateWidget, required=True)

    

    def clean_phone_no(self):
        phone_no = self.cleaned_data.get('phone_no')
        if phone_no and not phone_no.isdigit():
            raise forms.ValidationError('Phone number must contain only digits.')
        return phone_no

    def clean_email_id(self):
        email_id = self.cleaned_data.get('email_id')
        if email_id and Clients.objects.filter(email_id=email_id).exists():
            raise forms.ValidationError('Email ID already exists.')
        return email_id

    def clean_due_date(self):
        due_date = self.cleaned_data.get('due_date')
        if due_date and due_date <= date.today():
            raise forms.ValidationError('Due date must be in the future.')
        return due_date

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['job_id', 'prod_name', 'category', 'brand', 'model', 'description']
        widgets = {
            'job_id': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Job ID'
            }),
            'prod_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Product Name'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control'
            }),
            'brand': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Brand'
            }),
            'model': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Model'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Enter Description'
            }),
        }


class ClientForm(forms.ModelForm):
    class Meta:
        model = Clients
        fields = ['client_id', 'first_name', 'last_name', 'phone_no', 'email_id', 'address', 'job_id']
        widgets = {
            'client_id': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Client ID'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter First Name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Last Name'
            }),
            'phone_no': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Phone Number',
                'type': 'tel'
            }),
            'email_id': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Email Address'
            }),
            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Address',
                'rows': 4
            }),
            'job_id': forms.Select(attrs={
                'class': 'form-control'
            }),
        }


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Services
        fields = ['service_id', 'client_id', 'job_id', 'priority', 'status', 'due_date']
        widgets = {
            'service_id': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Service ID',
            }),
            'client_id': forms.Select(attrs={
                'class': 'form-select',
            }),
            'job_id': forms.Select(attrs={
                'class': 'form-select',
            }),
            'priority': forms.Select(attrs={
                'class': 'form-select',
            }),
            'status': forms.Select(attrs={
                'class': 'form-select',
            }),
            'due_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            }),
        }


class PostServicesForm(forms.ModelForm):
    class Meta:
        model = PostServices
        fields = ['job_id','prod_name', 'user_description','prod_description', 'work_hours']
        widgets = {
            'job_id': forms.Select(attrs={
                'class': 'form-select',
            }),
            'prod_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Product Name',
            }),
            'user_description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Enter User Description',
            }),
            'prod_description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Enter Product Description',
            }),
            'work_hours': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Work Hours',
            }),
        }

    def __init__(self, *args, **kwargs):
        super(PostServicesForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['prod_name'].initial = self.instance.job_id.prod_name
            self.fields['user_description'].initial = self.instance.job_id.description
        elif 'initial' in kwargs and 'job_id' in kwargs['initial']:
            job_id = kwargs['initial']['job_id']
            product = Products.objects.get(pk=job_id)
            self.fields['prod_name'].initial = product.prod_name
            self.fields['user_description'].initial = product.description