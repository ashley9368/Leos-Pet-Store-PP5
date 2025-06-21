from django.urls import path
from .views import newsletter_signup, subscribe, unsubscribe

urlpatterns = [
    path('', newsletter_signup, name='newsletter_signup'),
    path('subscribe/', subscribe, name='subscribe'),
    path('unsubscribe/<uuid:token>/', unsubscribe, name='unsubscribe'),
]