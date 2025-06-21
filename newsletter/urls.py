from django.urls import path
from .views import newsletter_signup, subscribe

urlpatterns = [
    path('', newsletter_signup, name='newsletter'),
    path('subscribe/', subscribe, name='subscribe'),
]