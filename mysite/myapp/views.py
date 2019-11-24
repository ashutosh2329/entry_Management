from django.shortcuts import render
from django.http import HttpResponse
from .models import Host

# Create your views here.

def index(request):
    hosts = Host.objects.all()
    context = {
        'hosts':hosts
    }

    return render(request,"myapp_home.html",context);
