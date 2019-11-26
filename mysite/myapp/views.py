from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Host, Visitor
from datetime import datetime

from django.views.generic import TemplateView

from .forms import VisitorForm, HostForm


class HomeView(TemplateView):

    def get(self, request):
        hosts = Host.objects.all()
        current_visitor = Visitor.objects.all().filter(present=True)
        if len(current_visitor)>0:
            flag = True
        else:
            flag = False
        context = {
            'hosts':hosts,
            'visiters':current_visitor,
            'flag':flag,
        }
        return render(request,"myapp_home.html",context)

    def post(self, request):
        VisitorsChekingout = request.POST.getlist('checks')
        # if len(VisitorsChekingout)<= 0:
        #     return redirect(self.get(msg="check the box for checking out"))
        for vi_id in VisitorsChekingout:
            Visitor_object = Visitor.objects.all().filter(id=vi_id)
            Visitor.checkout(Visitor_object[0])
        
        current_visitor = Visitor.objects.all().filter(present=True)
        if len(current_visitor)>0:
            flag = True
        else:
            flag = False
        context = {
            'visiters':current_visitor,
            'flag':flag
        }
        return render(request,'myapp_home.html',context)

class HostView(TemplateView):
    form = HostForm()

    def get(self, request):
        
        context = {
            'form':self.form,
            'error': ""
        }
        return render(request,'addHost.html',context)

    def post(self, request):
        form = HostForm(request.POST)
        if form.is_valid():
            form.save()
            msg = form.cleaned_data['name'] + " successfuly Added as host"
        else:
            error = "fill fields correctly"
            context = {
                'form':self.form,
                'error':error
            }
            return render(request,'addHost.html',context)
        context = {
            'msg':msg
        }
        return render(request,'addHostSuccess.html',context)

class CheckinView(TemplateView):
    form = VisitorForm()

    def get(self, request):
        
        context = {
            'form':self.form,
            'error':""
        }
        return render(request,'checkinVisitor.html',context)

    def post(self, request):
        form = VisitorForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = "fill details correctly/properly"
            context = {
                'form':self.form,
                'error':error
            }
            return render(request,'checkinVisitor.html',context)
        
        return redirect("/myapp")