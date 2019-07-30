
from django.urls import path
from . import views

urlpatterns = [
   


    path('drink',views.drinkOrdering,name='drorder'),
    path('food',views.foodOrder,name='foodorder'),
    path('dessert',views.dessertOrdering,name='desertorder'),




]
