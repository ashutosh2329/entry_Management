from django.shortcuts import render
from django.http import HttpResponse
from .models import Host, Visitor
from datetime import datetime

from django.views.generic import TemplateView

from .forms import VisitorForm, HostForm

# Create your views here.

def index(request):
    hosts = Host.objects.all()
    current_visitor = Visitor.objects.all().filter(present=True)
    context = {
        'hosts':hosts,
        'visiters':current_visitor
    }
    return render(request,"myapp_home.html",context)


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