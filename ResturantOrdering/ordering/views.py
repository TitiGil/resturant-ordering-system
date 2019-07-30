from django.shortcuts import render
from .models import Drink,Dessert,Food
from django.http import Http404

def home(request):
    return render(request,'home.html')

def foodOrder(request):
    food=Food.objects.all()
    return render(request,'foodOrdering.html',{'food':food})

def drinkOrdering(request):
    drink=Drink.objects.all()
    return render(request,'drinkOrdering.html',{'drink':drink})

def dessertOrdering(request):
    dessert=Dessert.objects.all()
    return render(request,'dessertOrdering.html',{'dessert':dessert})
def notFound(request):
    raise Http404("page Not Found")

