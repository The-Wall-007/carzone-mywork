from django.urls import path
from .views import login,register,dashboard,logout

urlpatterns = [
    path('login', login,name='login_page'),
    path('register', register,name='register_page'),
    path('dashboard', dashboard,name='dashboard_page'),
    path('logout', logout,name='logout'),
    
]
