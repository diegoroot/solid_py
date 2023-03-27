from django.urls import path
from .views import CreateUser

urlpatterns = [
    path('create_user/', CreateUser.as_view(), name='user_create_view'),
]
