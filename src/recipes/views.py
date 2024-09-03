from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
# from django.urls import reverse
from .models import Recipe

#to protect class-based view
from django.contrib.auth.mixins import LoginRequiredMixin # protecting this view requiring the user to login to view it


# Create your views here.

def home(request):
    return render(request, 'recipe/recipes_home.html')

class RecipeListView(LoginRequiredMixin, ListView): #Add LoginReq here to protect this view
    model = Recipe
    template_name = 'recipes/recipe_overview.html'

class RecipeDetailView(LoginRequiredMixin, DetailView): #Loginreq here to protect this view too 
    model = Recipe
    template_name = 'recipes/recipe_detail.html'

def recipe_overview(request):
    recipes = Recipe.objects.all()
    return render(request, "recipe/recipe_overview.html", {"recipes": recipes})


def recipe_detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    difficulty = recipe.calculate_difficulty()
    return render(
        request, "recipe/recipe_detail.html", {"recipe": recipe, "difficulty": difficulty}
    )


def search_by_ingredient(request):
    query = request.GET.get("query")
    if query:
        recipes = Recipe.objects.filter(ingredients__name__icontains=query).distinct()
    else:
        recipes = Recipe.objects.none()
    return render(request, "recipe/search_results.html", {"recipes": recipes})

def search_results(request):
    query = request.GET.get('query')
    recipes = Recipe.objects.filter(ingredients__name__icontains=query) if query else Recipe.objects.none()
    return render(request, 'recipe/search_results.html', {'recipes': recipes})

""" def search_results(request):
    query = request.GET.get("query", "")
    if query:
        ingredients = Ingredient.objects.filter(name__icontains=query)
        recipes = Recipe.objects.filter(ingredients__in=ingredients).distinct()
    else:
        recipes = Recipe.objects.none()

    return render(request, "search_results.html", {"recipes": recipes}) """