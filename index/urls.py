from django.urls import path
from . import views
from .views import (
    index,
    dump_database_view
)


# app_name='stories'

urlpatterns = [
    path('', views.index, name='index_page'),
    path('dump/', views.dump_database_view, name='dump'),

    # path('about/', views.about, name='stories-about'),
    # path('stories/', views.stories, name='stories-stories'),
    # path('recipes/<slug:slug>/', RecipeDetailView.as_view(), name='recipe_detail_url'),
    # path('recipes/', RecipeListView.as_view(), name='stories-recipes'),

    # path('contact/', views.contact, name='stories-contact'),
    # path('recipes/', views.recipes, name='stories-recipes'),
]
