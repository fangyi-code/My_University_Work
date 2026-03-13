from django.urls import path

from . import views 

urlpatterns = [
    path('orders/',views.listorders),
    path('customers/',views.listcustomers),
]