from django.urls import path
from . import views

# import home view
from .views import home

from .views import RecipeListView, RecipeDetailView

app_name = 'recipe'

urlpatterns = [
    # path("", home),
    path("", views.home, name="home"),
    path("list/", RecipeListView.as_view(), name="list"),
    path("list/<pk>", RecipeDetailView.as_view(), name="detail"),
    path("recipes/", views.recipe_overview, name="recipe_overview"),
    path("recipes/<int:pk>/", views.recipe_detail, name="recipe_detail"),
    path("search/", views.search_results, name="search_results"),
     path('overview/', views.recipe_overview, name='overview'),
]

