from django.urls import path
from .views import CreatePaymentBank

urlpatterns = [
    path('create/', CreatePaymentBank.as_view(), name='payment_create_view'),
]
