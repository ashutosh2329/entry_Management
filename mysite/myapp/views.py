from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Host, Visitor
from datetime import datetime

from django.views.generic import TemplateView

from .forms import VisitorForm, HostForm

from django.core.mail import send_mail
from django.conf import settings

def email(request,subject,message,recipient):
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [recipient,]
    send_mail( subject, message, email_from, recipient_list )


class HomeView(TemplateView):

    def get(self, request):
        print("get herer")
        current_visitor = Visitor.objects.all().filter(present=True)
        if len(current_visitor)>0:
            flag = True
        else:
            flag = False
        context = {
            'visiters':current_visitor,
            'flag':flag,
        }
        return render(request,"myapp_home.html",context)

    def post(self, request):
        print("post here")
        VisitorsChekingout = request.POST.getlist('checks')
        for vi_id in VisitorsChekingout:
            Visitor_object = Visitor.objects.all().filter(id=vi_id)[0]
            Visitor.checkout(Visitor_object)
            message = "Hi Your Visitor name: "+Visitor_object.name+" email: "+Visitor_object.email+" phone number : "+str(Visitor_object.phone)+" checkin time "+str(Visitor_object.checkin_time)+" is checking out";
            recipient = Visitor_object.visiting_host.email
            email(request,subject="Checkout Visitor",message=message,recipient=recipient)
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
            message = "Hi you have a visitor name: "+str(form.cleaned_data['name'])+" email: "+str(form.cleaned_data['email'])+" phone number : "+str(form.cleaned_data['phone'])+" ";
            recipient = form.cleaned_data['visiting_host'].email
            email(request,subject="Checkin Visitor",message=message,recipient=recipient)
        else:
            error = "fill details correctly/properly"
            context = {
                'form':self.form,
                'error':error
            }
            return render(request,'checkinVisitor.html',context)
        
        return redirect("/myapp")