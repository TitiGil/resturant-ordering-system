from django.contrib import admin

# Register your models here.
from .models import Food,Drink,Dessert

@admin.register(Food)

class FoodAdmin(admin.ModelAdmin):
    list_display=['name','price','amount']
    list_filter=('name','price')
    
    pass

@admin.register(Drink)

class DrinkAdmin(admin.ModelAdmin):
    list_display=['name','price','amount','kind']
    
    pass

@admin.register(Dessert)

class DessertAdmin(admin.ModelAdmin):
    list_display=['name','price','amount']
    pass
    
