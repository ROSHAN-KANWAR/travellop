from django.db import models

#contact
class Contact(models.Model):
    subject=models.CharField(max_length=34)
    name=models.CharField(max_length=35)
    email=models.EmailField(max_length=56)
    message=models.CharField(max_length=67)

#subscribe for database
class Subscribe(models.Model):
    name=models.CharField(max_length=35)
    email=models.EmailField(max_length=56)
   
#destinamtion

class Destination(models.Model):
    Image = models.ImageField()
    title=models.CharField(max_length=40)
    descrip=models.CharField(max_length=50)
    price=models.IntegerField()
    
class Destination1(Destination):
    star=models.CharField(max_length=23)
    all=models.CharField(max_length=43)
    ticket=models.CharField(max_length=45)
    visits=models.CharField(max_length=20)


#best trip
class Besttrip(models.Model):
   date = models.IntegerField()
   month = models.CharField(max_length=20)
   Image = models.ImageField()
   link = models.CharField(max_length=23)
   descrip = models.CharField(max_length=50)
   title = models.CharField(max_length=40)
   
#newstrip
class Newstrip(Besttrip):
   title1 = models.CharField(max_length=40)

#Team About
class Team(models.Model):
    Image = models.ImageField()
    title = models.CharField(max_length=40)
    descrip = models.CharField(max_length=80)
