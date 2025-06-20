from django.urls import path
from . import views
from .views import vote_product

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('toggle-visibility/<int:pk>/', views.toggle_visibility, name='toggle_visibility'),
    path('review/delete/<int:review_id>/', views.delete_review, name='delete_review'),
    path('<int:product_id>/vote/<str:vote_type>/', vote_product, name='vote_product'),
]
