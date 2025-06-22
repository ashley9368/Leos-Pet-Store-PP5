from django.urls import path
from .views import newsletter_signup, subscribe
from . import views

urlpatterns = [
    path('', newsletter_signup, name='newsletter'),
    path('subscribe/', subscribe, name='subscribe'),
    path('unsubscribe/<uuid:token>/', views.unsubscribe, name='unsubscribe'),
]