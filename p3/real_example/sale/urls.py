from django.urls import path
from .views import CreateSale

urlpatterns = [
    path('create/', CreateSale.as_view(), name='sale_create_view'),
]
