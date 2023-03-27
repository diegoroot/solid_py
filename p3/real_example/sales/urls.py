from django.urls import path
from .views import CreateSales

urlpatterns = [
    path('create/', CreateSales.as_view(), name='sales_create_view'),
]
