from django.urls import path
from .views import HostView, CheckinView, HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('addHost',HostView.as_view(),name='adding host'),
    path('checkinVisitor',CheckinView.as_view(),name='checkin visitor'),
]