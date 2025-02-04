from django.shortcuts import render, redirect, get_object_or_404
from .forms import CombinedForm, ProductForm, ClientForm, ServiceForm, PostServicesForm
from .models import Clients, Products, Services, PostServices


def home(request):
    return render(request,'structure/home.html')

def products(request):
    products = Products.objects.all()
    return render(request,'structure/products.html',{'products': products})

def customers(request):
    clients = Clients.objects.all()
    return render(request,'structure/customers.html',{'clients': clients})

def services(request):
    services=Services.objects.all()
    return render(request,'structure/service.html',{'services': services})

def post_services(request):
    products = Products.objects.all()
    postservices=PostServices.objects.all()
    return render(request,'structure/post_service.html',{'postservices': postservices, 'products': products})

def reviews(request):
    return render(request,'structure/reviews.html')

def success_view(request):
    return render(request, 'structure/success.html')


def combined_view(request):
    if request.method == 'POST':
        form = CombinedForm(request.POST)
        if form.is_valid():
            # Save product data
            product_data = {
                'job_id': form.cleaned_data['job_id'],
                'prod_name': form.cleaned_data['prod_name'],
                'category': form.cleaned_data['category'],
                'brand': form.cleaned_data['brand'],
                'model': form.cleaned_data['model'],
                'description': form.cleaned_data['description'],
            }
            product = Products.objects.create(**product_data)

            # Save client data
            client_data = {
                'client_id': form.cleaned_data['client_id'],
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'phone_no': form.cleaned_data['phone_no'],
                'email_id': form.cleaned_data['email_id'],
                'address': form.cleaned_data['address'],
                'job_id': product,
            }
            client = Clients.objects.create(**client_data)

            # Save service data
            service_data = {
                'service_id': form.cleaned_data['service_id'],
                'client_id': client,
                'job_id': product,
                'priority': form.cleaned_data['priority'],
                'status': form.cleaned_data['status'],
                'due_date': form.cleaned_data['due_date'],
            }
            Services.objects.create(**service_data)

            return redirect('success')  # Redirect to the success page
        else:
            # Print form errors for debugging
            print(form.errors)
    else:
        form = CombinedForm()

    return render(request, 'structure/combined_template.html', {'form': form})




#ALL THINGS PRODUCTS

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('products')
    else:
        form = ProductForm()
    return render(request, 'structure/add_product.html', {'form': form})

def edit_product(request, pk):
    products = get_object_or_404(Products, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=products)
        if form.is_valid():
            form.save()
            return redirect('products')  # Replace with your product list view name
    else:
        form = ProductForm(instance=products)
    return render(request, 'structure/edit_product.html', {'form': form})

# Delete Product
def delete_product(request, pk):
    products = get_object_or_404(Products, pk=pk)
    if request.method == "POST":
        products.delete()
        return redirect('products')  # Replace with your product list view name
    return render(request, 'structure/delete_product.html', {'products': products})




#ALL THINGS CLIENT

def add_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('customers')
    else:
        form = ClientForm()
    return render(request, 'structure/add_client.html', {'form': form})

def edit_client(request, pk):
    client = get_object_or_404(Clients, pk=pk)
    if request.method == "POST":
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('customers')  # Replace with your client list view name
    else:
        form = ClientForm(instance=client)
    return render(request, 'structure/edit_client.html', {'form': form})

# Delete Client
def delete_client(request, pk):
    client = get_object_or_404(Clients, pk=pk)
    if request.method == "POST":
        client.delete()
        return redirect('customers')  # Replace with your client list view name
    return render(request, 'structure/delete_client.html', {'client': client})





#ALL THINGS SERVICE

def add_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('services')
    else:
        form = ServiceForm()
    return render(request, 'structure/add_service.html', {'form': form})

def edit_service(request, pk):
    service = get_object_or_404(Services, pk=pk)
    if request.method == "POST":
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('services')  # Replace with your service list view name
    else:
        form = ServiceForm(instance=service)
    return render(request, 'structure/edit_service.html', {'form': form})

# Delete Service
def delete_service(request, pk):
    service = get_object_or_404(Services, pk=pk)
    if request.method == "POST":
        service.delete()
        return redirect('services')  # Replace with your service list view name
    return render(request, 'structure/delete_service.html', {'service': service})



#ALL THINGS POST SERVICE

def add_post_service(request):
    if request.method == 'POST':
        form = PostServicesForm(request.POST)
        if form.is_valid():
            # Fill prod_name and prod_description based on job_id
            job_id = form.cleaned_data['job_id']
            form.instance.prod_name = job_id.prod_name
            form.instance.user_description = job_id.description
            form.save()
            return redirect('postservices')
    else:
        form = PostServicesForm()
    return render(request, 'structure/add_post_service.html', {'form': form}) 

def edit_post_service(request, pk):
    postservices = get_object_or_404(PostServices, pk=pk)
    if request.method == 'POST':
        form = PostServicesForm(request.POST, instance=postservices)
        if form.is_valid():
            form.save()
            return redirect('postservices')
    else:
        form = PostServicesForm(instance=postservices)
    return render(request, 'structure/edit_post_service.html', {'form': form})

def delete_post_service(request, pk):
    postservices = get_object_or_404(PostServices, pk=pk)
    if request.method == 'POST':
        postservices.delete()
        return redirect('postservices')
    return render(request, 'structure/delete_post_service.html', {'postservices': postservices})






def ongoing_services(request):
    # Filter services with status 'Completed'
    completedd_services = Services.objects.filter(status='PENDING')
    
    # Collect necessary data
    ongoing_services = []
    for service in completedd_services:
        product = Products.objects.get(job_id=service.job_id.job_id)
        client = Clients.objects.get(client_id=service.client_id.client_id)
        ongoing_services.append({
            'job_id': product.job_id,
            'prod_name': product.prod_name,
            'status': service.status,
            'due_date': service.due_date,
            'client_name': f"{client.first_name} {client.last_name}"
        })

    context = {
        'ongoing_services': ongoing_services
    }
    return render(request, 'structure/ongoing_services.html', context)


def completed_services(request):
    # Filter services with status 'Completed'
    done_services = Services.objects.filter(status='FINISHED')
    
    # Collect necessary data
    completed_services = []
    for service in done_services:
        product = Products.objects.get(job_id=service.job_id.job_id)
        client = Clients.objects.get(client_id=service.client_id.client_id)
        completed_services.append({
            'job_id': product.job_id,
            'prod_name': product.prod_name,
            'status': service.status,
            'due_date': service.due_date,
            'client_name': f"{client.first_name} {client.last_name}"
        })

    context = {
        'completed_services': completed_services
    }
    return render(request, 'structure/completed_services.html', context)