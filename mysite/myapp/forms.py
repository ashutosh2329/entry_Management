from django import forms

from .models import Visitor, Host

class VisitorForm(forms.ModelForm):

    class Meta:
        model = Visitor
        fields = ('name', 'email','phone','visiting_host','checkin_time')
    
class HostForm(forms.ModelForm):

    class Meta:
        model = Host
        fields = ('name','email','phone')