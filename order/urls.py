from django.urls import path
from django.conf.urls.static import static

from . import views
from .views import (
    cart,
)


urlpatterns = [
    path('cart/', views.cart, name='cart'),
    # path('product/<slug:slug>/', views.product_detail, name='product-detail'),
    # path('product/', views.product_page, name='product_page'),


    # path('about/', views.about, name='stories-about'),
    # path('stories/', views.stories, name='stories-stories'),
    # path('recipes/<slug:slug>/', RecipeDetailView.as_view(), name='recipe_detail_url'),
    # path('recipes/', RecipeListView.as_view(), name='stories-recipes'),

    # path('contact/', views.contact, name='stories-contact'),
    # path('recipes/', views.recipes, name='stories-recipes'),
]