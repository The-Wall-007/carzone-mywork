from django.shortcuts import render,redirect
from .models import Team
from Cars.models import Car
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.
def home(request):
    team_data = Team.objects.all()
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    cars = Car.objects.order_by('-created_date')
    #search_fields = Car.objects.values('model','city','year','body_style')
    model_search = Car.objects.order_by().values_list('model',flat=True).distinct()
    body_style = Car.objects.order_by().values_list('body_style',flat=True).distinct()
    year_search = Car.objects.order_by().values_list('year',flat=True).distinct()
    states = Car.objects.values_list('state',flat=True).distinct()
    context = {
        'TD' : team_data,
        'featured_cars' : featured_cars,
        'cars' : cars,
        #'sf' : search_fields
        'model_search' : model_search,
        'year_search' : year_search,
        'body_style' : body_style,
        'states' : states,
    }
    print(request.path)
    return render(request,'Pages/Home.html',context)

def about(request):
    team_data = Team.objects.all()
    context = {
        'TD' : team_data
    }
    print(request.path)
    return render(request,'Pages/about.html',context)

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        phone = request.POST['phone']
        subject = request.POST['subject']

        email_subject = "You have a new message from Carzone website regarding " + subject
        message_body = "Name: " + name + ". Email: " + email + ". Phone. " + phone + ". Message: " + message

        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        send_mail(
            email_subject,
            message_body,
            'dvlpatel2410@gmail.com',
            [admin_email],
            fail_silently=False
        )

        messages.success(request,"Thank you for contacting us. We'll reach you soon.")
        return redirect('contact')
    
    return render(request,'Pages/contact.html')

def service(request):
    return render(request,'Pages/services.html')