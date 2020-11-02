from django.urls import path, include
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('sign', views.sign, name='sign'),
]
