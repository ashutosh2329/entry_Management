from django.contrib import admin

# Register your models here.
from .models import Visitor, Host;

admin.site.register(Visitor);
admin.site.register(Host);