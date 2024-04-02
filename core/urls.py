from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('services/<slug:service_id>/', views.service_detail, name="service"),
    path('send_email/', views.sendEmail, name='mail'),
    path('payment/', views.payment, name='payment'),
]
