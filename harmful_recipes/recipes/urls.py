from django.urls import path
from . import views


urlpatterns = [
    path('full_recipe/<int:recipe_id>/', views.full_recipe, name='full_recipe'),
    path('meat/<int:recipe_id>/', views.meat_recipe, name='meat'),
    path('fish/<int:recipe_id>/', views.fish_recipe, name='fish'),
    path('hen/<int:recipe_id>/', views.hen_recipe, name='hen'),
    path('exp/', views.exp, name='exp'),
    path('user_form/', views.user_form, name='user_form'),
    path('recipe_form/', views.recipe_form, name='recipe_form'),
    path('all_recipes/', views.all_recipes, name='all_recipes'),
    path('edit_recipe/<int:recipe_id>/', views.edit_recipe, name='edit_recipe'),
    path('upload_image/<int:recipe_id>/', views.upload_image, name='upload_image'),
    path("task_of_the_day/", views.task_of_the_day, name="task_of_the_day"),
]