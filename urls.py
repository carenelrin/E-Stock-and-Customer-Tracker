from django.urls import path
from . import views

urlpatterns=[
    path('home/',views.home,name="home"),
    path('',views.home,name="home"),
   
   
    
    
    path('reviews/',views.reviews,name="reviews"),
    path('combined_template/',views.combined_view,name="combined"),
    path('success/', views.success_view, name='success'),
    
    #Post Service URLs
    path('postservices/',views.post_services,name="postservices"),
    path('add_post_service/', views.add_post_service, name='add_post_service'),
    path('edit_post_service/<int:pk>/', views.edit_post_service, name='edit_post_service'),
    path('delete_post_service/<int:pk>/', views.delete_post_service, name='delete_post_service'),

    #Product URLs
    path('products/',views.products,name="products"),
    path('add_product/', views.add_product, name='add_product'),
    path('edit_product/<int:pk>/', views.edit_product, name='edit_product'),
    path('delete_product/<int:pk>/', views.delete_product, name='delete_product'),

    # Client URLs
    path('customers/',views.customers,name="customers"),
    path('add_client/', views.add_client, name='add_client'),
    path('edit_client/<int:pk>/', views.edit_client, name='edit_client'),
    path('delete_client/<int:pk>/', views.delete_client, name='delete_client'),

    # Service URLs
    path('services/',views.services,name="services"),
    path('add_service/', views.add_service, name='add_service'),
    path('edit_service/<int:pk>/', views.edit_service, name='edit_service'),
    path('delete_service/<int:pk>/', views.delete_service, name='delete_service'),

    path('ongoing_services/', views.ongoing_services, name='ongoing_services'),
    path('completed_services/', views.completed_services, name='completed_services'),
]