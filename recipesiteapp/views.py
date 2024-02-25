from django.core.files.storage import FileSystemStorage
from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404
from .models import Recipes
from .forms import RecipeForm, UpdateRecipeForm
from random import choice


def index(request: HttpRequest):
    recipe = Recipes.objects.all()
    results = [choice(recipe) for _ in range(0, 5)]
    context = {"results": results}
    return render(request, 'recipesiteapp/index.html', context)


def recipe_page(request: HttpRequest, recipe_id):
    recipe = get_object_or_404(Recipes, pk=recipe_id)
    return render(request, 'recipesiteapp/recipe.html', {'recipe': recipe})


def all_recipe(request):
    recipe = Recipes.objects.all()
    context = {'title': recipe}
    return render(request, 'recipesiteapp/all_recipe.html', context)


def new_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.cleaned_data['photo']
            fs = FileSystemStorage()
            fs.save(photo.name, photo)
            recipe = form.save()
            return recipe_page(request, recipe.pk)
        else:
            return render(request, 'recipesiteapp/new_recipe.html', {'form': form})
    return render(request, 'recipesiteapp/new_recipe.html', {'form': RecipeForm})


def update_recipe(request, recipe_id):
    recipe = Recipes.objects.filter(pk=recipe_id).first()
    if request.method == 'POST':
        form = UpdateRecipeForm(request.POST, request.FILES)
        message = 'Ошибка в данных'
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            steps_cooking = form.cleaned_data['steps_cooking']
            time_for_cooking = form.cleaned_data['time_for_cooking']
            photo = form.cleaned_data['photo']

            fs = FileSystemStorage()
            fs.save(photo.name, photo)

            recipe.title = title
            recipe.description = description
            recipe.steps_cooking = steps_cooking
            recipe.time_for_cooking = f'{time_for_cooking} мин'
            recipe.photo = photo.name

            recipe.save()
            return recipe_page(request, recipe.pk)
    else:
        form = UpdateRecipeForm()
        message = 'Отредактируйте рецепт'
    return render(request, 'recipesiteapp/update_recipe.html', {'form': form, 'message': message})
