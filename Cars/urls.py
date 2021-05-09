from django.urls import path
from .views import car,carDetail,Search

urlpatterns = [
    path('', car,name='car'),
    path('<int:id>', carDetail,name='car_detail'),
    path('search', Search,name='search_page'),
]
