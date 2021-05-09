from django.urls import path
from .views import home,about,contact,service
urlpatterns = [
    path('', home,name='home'),
    path('about/', about,name='about'),
    path('contact/', contact,name='contact'),
    path('service/', service,name='service'),
]
