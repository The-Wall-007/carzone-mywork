from django.shortcuts import render,get_object_or_404
from .models import Car
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.
def car(request):
    car_data = Car.objects.order_by('-created_date')
    paginator = Paginator(car_data,1)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)

    #Search
    model_search = Car.objects.order_by().values_list('model',flat=True).distinct()
    body_style = Car.objects.order_by().values_list('body_style',flat=True).distinct()
    year_search = Car.objects.order_by().values_list('year',flat=True).distinct()
    states = Car.objects.values_list('state',flat=True).distinct()


    context = {
        "cd" : paged_cars,
        'model_search' : model_search,
        'year_search' : year_search,
        'body_style' : body_style,
        'states' : states,
    }
    return render(request,"Cars/car.html",context)

def carDetail(request,id):
    single_car = get_object_or_404(Car,pk=id)
    print(single_car)
    context = {
        'sc' : single_car
    }
    return render(request,"Cars/car_detail.html",context)

def Search(request):
    print(request.GET)
    car_data = Car.objects.order_by('-created_date')

    #Search
    model_search = Car.objects.order_by().values_list('model',flat=True).distinct()
    body_style = Car.objects.order_by().values_list('body_style',flat=True).distinct()
    year_search = Car.objects.order_by().values_list('year',flat=True).distinct()
    states = Car.objects.values_list('state',flat=True).distinct()
    transmission_search = Car.objects.values_list('transmission',flat=True).distinct()
    
    if "feature" in request.GET:
        feature = request.GET["feature"]
        if feature:
            car_data = car_data.filter(description__icontains=feature)
    if "model" in request.GET:
        model = request.GET["model"]
        if model:
            car_data = car_data.filter(model__icontains=model)
    if "location" in request.GET:
        location = request.GET["location"]
        if location:
            car_data = car_data.filter(state__icontains=location)
    if "year" in request.GET:
        year = request.GET["year"]
        if year:
            car_data = car_data.filter(year__icontains=year)
    if "type" in request.GET:
        typo = request.GET["type"]
        if typo:
            car_data = car_data.filter(body_style__icontains=typo)

    if "transmission" in request.GET:
        transmission = request.GET["transmission"]
        if transmission:
            car_data = car_data.filter(transmission__icontains=transmission)

    if "min_price" in request.GET:
        min_price = request.GET["min_price"]
        max_price = request.GET["max_price"]
        if max_price:
            car_data = car_data.filter(price__gte=min_price,price__lte=max_price)
    print(transmission)
    context = {
        "cd" : car_data,
        'model_search' : model_search,
        'year_search' : year_search,
        'body_style' : body_style,
        'states' : states,
        'transmission' : transmission_search,
    }
    return render(request,"Cars/search.html",context)