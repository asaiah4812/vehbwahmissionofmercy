from django.shortcuts import render, get_object_or_404
from . models import *
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

# Create your views here.

def home(request):   
    galleries = Gallery.objects.all()[:8]
    comments = Comment.objects.all()
    context = {
        'galleries':galleries,
        'comments':comments
    }
    return render(request, 'mission/home.html', context)

def about(request):
    abouts = About.objects.all()
    galleries = Gallery.objects.all()
    context = {
        'abouts':abouts,
        'galleries':galleries,
    }
    return render(request, 'mission/about.html', context)


def contact(request):
    context = {

    }
    return render(request, 'mission/contact.html', context)

def services(request):
    services = Service.objects.all()
    comments = Comment.objects.all()
    context = {
        "services": services,
        'comments': comments
    }
    return render(request, 'mission/services.html', context)

def service_detail(request, service_id):
    service = get_object_or_404(Service, slug=service_id)
    return render(request, 'mission/service_detail.html', {'service': service})

def sendEmail(request):
    if request.method == 'POST':
        template = render_to_string('email/email_templates.html', {
            "name": request.POST['name'],
            "email": request.POST['email'],
            "message": request.POST['message'],
        })
        email = EmailMessage(
            request.POST['subject'],
            template,
            settings.EMAIL_HOST_USER,
            ['henchon1@gmail.com'],
        )

        email.fail_silently=False
        email.send()
    return render(request, 'email/email_templates.html') 