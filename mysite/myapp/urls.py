from django.urls import path

from . import views
from .views import HostView, CheckinView

urlpatterns = [
    path('', views.index, name='index'),
    path('addHost',HostView.as_view(),name='adding host'),
    path('checkinVisitor',CheckinView.as_view(),name='checkin visitor'),
    path('checkoutVisitor',views.checkoutVisitor,name='checkout visitor')
]