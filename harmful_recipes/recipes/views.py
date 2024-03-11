import datetime
from random import choice

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import logging
from . forms import *
from recipes.models import Recipe, User
from . models import *

logger = logging.getLogger(__name__)

def full_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)

    return render(request, 'recipes/full_recipe.html', {'recipe': recipe})

def meat_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'recipes/meat_recipe.html', {'recipe': recipe})

def fish_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'recipes/fish_recipe.html', {'recipe': recipe})

def hen_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'recipes/hen_recipe.html', {'recipe': recipe})

def exp(request):
    recipes = Recipe.objects.all()
    users=User.objects.all()
    random_recipes_list = []
    i=0
    while i < 5:
        new_recipe = get_object_or_404(Recipe, pk=choice (range(1, len(recipes))))
        if new_recipe not in random_recipes_list:
            random_recipes_list.append(new_recipe)
            i+=1

    return render(request, 'recipes/exp.html', {'recipes': random_recipes_list, 'users': users})

def user_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            password = form.cleaned_data['password']
            status = form.cleaned_data['status']
            avatar = form.cleaned_data['avatar']
            user = User(name=name, email=email, age=age, password=password,status=status, avatar=avatar)
            user.save()
    else:
        form = UserForm()
    return render(request, 'recipes/user_form.html', {'form': form})

def recipe_form(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            ingredients = form.cleaned_data['ingredients']
            cooking_process = form.cleaned_data['cooking_process']
            cooking_time = form.cleaned_data['cooking_time']
            amount_of_servings = form.cleaned_data['amount_of_servings']
            calories = form.cleaned_data['calories']
            image = form.cleaned_data['image']
            recipe = Recipe(name=name,
                            description=description,
                            ingredients=ingredients,
                            cooking_process=cooking_process,
                            cooking_time=cooking_time,
                            amount_of_servings=amount_of_servings,
                            calories=calories,
                            image=image)
            recipe.save()
    else:
        form = RecipeForm()
    return render(request, 'recipes/recipe_form.html', {'form': form})


def all_recipes(request):
    recipes = Recipe.objects.all()
    users=User.objects.all()
    return render(request, 'recipes/all_recipes.html', {'recipes': recipes, 'users': users})

def edit_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    form = RecipeForm()
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            ingredients = form.cleaned_data['ingredients']
            cooking_process = form.cleaned_data['cooking_process']
            cooking_time = form.cleaned_data['cooking_time']
            amount_of_servings = form.cleaned_data['amount_of_servings']
            calories = form.cleaned_data['calories']
            image = form.cleaned_data['image']
            recipe.name = name
            recipe.description = description
            recipe.ingredients = ingredients
            recipe.cooking_process = cooking_process
            recipe.cooking_time = cooking_time
            recipe.amount_of_servings = amount_of_servings
            recipe.calories = calories
            recipe.image = image
            recipe.save()
    else:
        form = RecipeForm()
    return render(request, 'recipes/edit_recipe.html', {'form': form, 'recipe': recipe})

def upload_image(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            recipe.image = image
            recipe.save()
    else:
        form = RecipeForm()
    return render(request, 'recipes/upload_image_form.html', {'form': form, 'recipe': recipe})

def task_of_the_day(request):
    current_date = datetime.datetime.now()
    if current_date.day % 2 == 0:
        task_list = ["Поколение Python Professional", "Databases", "Git", "Django", "English", "Linux"]
    else:
        task_list = ["Поколение Python Control", "OOP", "Asyncio", "Regex", "Собеседование"]
        return render(request, 'recipes/task_of_the_day.html', {'task_list': task_list})