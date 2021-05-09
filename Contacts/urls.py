from django.urls import path
from .views import inquiry

urlpatterns = [
   path('', inquiry,name='inquiry'),
]
