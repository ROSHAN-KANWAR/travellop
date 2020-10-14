from django.contrib import admin
from .models import Subscribe,Destination,Destination1,Besttrip,Team,Newstrip,Contact

#contat
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email','subject','message']

#Subscribe
@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display=['id','name','email']

#Destinations


@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display=['id','Image','title','descrip','price']

#Destinations1
@admin.register(Destination1)
class Destination1Admin(admin.ModelAdmin):
    list_display = ['id', 'Image', 'title', 'descrip', 'price']


#Besttrip
@admin.register(Besttrip)
class BesttripAdmin(admin.ModelAdmin):
    list_display = ['id','date','month', 'Image', 'title', 'descrip', 'link']


#Newstrip
@admin.register(Newstrip)
class NewstripAdmin(admin.ModelAdmin):
    list_display = ['id', 'date', 'month', 'Image', 'title', 'descrip', 'link']



#teamabout
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['id','Image', 'title', 'descrip']
