
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views
urlpatterns = [
    path('',views.Index,name='Home'),
    path('about/', views.About, name='About'),
    path('news/',views.News,name='News'),
    path('contact/',views.Contact,name='Contact'),
    path('destinamtions/',views.Des,name='Des'),
    path('elements/',views.Element,name='Ele'),
    path('submit/', views.Submit, name='submit'),
    path('submit/', views.Submit1, name='submit1'),
  


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
