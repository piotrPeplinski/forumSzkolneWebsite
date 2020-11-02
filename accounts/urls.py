from django.urls import path, include
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('sign', views.sign, name='sign'),
    path('logoutuser', views.logoutuser, name='logoutuser'),
    path('log',views.log,name='log'),
]
