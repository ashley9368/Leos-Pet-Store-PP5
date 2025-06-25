from django.urls import path
from . import views

urlpatterns = [
    path('toggle/<int:product_id>/',views.toggle_wishlist, name='toggle_wishlist'),
]