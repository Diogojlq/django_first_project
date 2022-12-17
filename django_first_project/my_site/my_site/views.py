from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# Create your views here.



def home(request):
    
    return render(request,'my_site/home.html')


def login_page(request):
    
    return render(request,'my_site/login.html')


def about_page(request):

    return render(request,'my_site/about.html')



def register_page(request):
    return render(request,'my_site/register.html')
