from django.urls import path, include
from .views import home, login

urlpatterns = [
    path('home/', home, name='home'),
    path('', login, name='login'),
    path('', include('django.contrib.auth.urls')),
]