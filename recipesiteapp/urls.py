from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recipe/<int:recipe_id>', views.recipe_page, name='recipe_page'),
    path('new_recipe/', views.new_recipe, name='new_recipe'),
    path('update_recipe/<int:recipe_id>', views.update_recipe, name='update_recipe'),
    path('all_recipe/', views.all_recipe, name='all_recipe'),
]
