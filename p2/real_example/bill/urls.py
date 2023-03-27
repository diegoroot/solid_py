from django.urls import path
from .views import Home, CreateBill

urlpatterns = [
    path('home/', Home, name='home'),
    path('create/', CreateBill.as_view(), name='bill_create_view'),
]
