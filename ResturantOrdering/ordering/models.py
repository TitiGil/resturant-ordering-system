from django.db import models

class Food(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField()
    amount=models.IntegerField()
    id=models.AutoField(primary_key=True)
    pass

class Drink(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField()
    amount=models.IntegerField()
    kind=models.CharField(choices=[('H','HOT'),('C','COLD')], max_length=50)
    id=models.AutoField(primary_key=True)
    pass

class Dessert(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField()
    amount=models.IntegerField()
  
    id=models.AutoField(primary_key=True)
    pass