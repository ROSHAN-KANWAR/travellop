from django.shortcuts import render
from .models import Subscribe, Destination,Destination1,Besttrip,Team,Newstrip,Contact
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.paginator import Paginator
# index
def Index(request):
    des=Destination.objects.all()
    best=Besttrip.objects.all()
    params={'des':des,'best':best}
    return render(request,'index.html',params)

#about
def About(request):
    team = Team.objects.all()
    params={'team':team}
    return render(request,'about.html',params)

#news
def News(request):
    post = Newstrip.objects.all().order_by('id')
    paginator = Paginator(post, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    team1 = Newstrip.objects.all().reverse()[:3]
    params={'team':page_obj,'team1':team1}
    return render(request,'news.html',params)

#contact
def Contact(request):
    return render(request,'contact.html')

#des
def Des(request):
    Des1=Destination1.objects.all()
    params={'Des1':Des1}
    return render(request,'destinations.html',params)

#ele
def Element(request):
    return render(request,'elements.html')

#subscibe database


def Submit(request):
           name = request.POST['name']
           ename = request.POST['email']
           data=Subscribe(name=name,email=ename)
           data.save() 
           return HttpResponseRedirect('/')

#contact
def Submit1(request):
    name = request.POST['name']
    ename = request.POST['email']
    sub = request.POST['subject']
    mess=request.POST['mess']
    data1 = Contact(name=name, email=ename, subject=sub,message=mess)
    data1.save()
    return HttpResponseRedirect('/')
