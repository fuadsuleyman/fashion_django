from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('product-list/', views.all_products, name="product-list"),
    path('product-detail/<str:pk>/', views.get_product, name="product-detail"),
    path('product-create/', views.create_product, name="product-create"),
    path('product-update/<str:pk>/', views.update_product, name="product-update"),
    path('product-delete/<str:pk>/', views.delete_product, name="product-delete"),
]