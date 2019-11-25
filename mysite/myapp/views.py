from django.shortcuts import render
from django.http import HttpResponse
from .models import Host
from datetime import datetime

from django.views.generic import TemplateView

from .forms import VisitorForm, HostForm

# Create your views here.

def index(request):
    hosts = Host.objects.all()
    context = {
        'hosts':hosts
    }
    return render(request,"myapp_home.html",context)

def checkoutVisitor(request):
    #print("test")
    return render(request,'checkoutVisitor.html')


# def addHost(request):
#     form = HostForm()
#     context = {
#         'form':form
#     }
#     return render(request,'addHost.html',context)

class HostView(TemplateView):
    template_name = 'myapp_home.html'

    def get(self, request):
        form = HostForm()
        context = {
            'form':form
        }
        return render(request,'addHost.html',context)

    def post(self, request):
        form = HostForm(request.POST)
        if form.is_valid():
            form.save()
        
        return render(request,'myapp_home.html')

# def checkinVisitor(request):
#     form = VisitorForm()
#     context = {
#         'form':form
#     }
#     return render(request,'checkinVisitor.html',context)

class CheckinView(TemplateView):
    template_name = 'myapp_home.html'

    def get(self, request):
        form = VisitorForm()
        context = {
            'form':form
        }
        return render(request,'checkinVisitor.html',context)

    def post(self, request):
        form = VisitorForm(request.POST)
        if form.is_valid():
            form.save()
        
        return render(request,'myapp_home.html')