from django.urls import path

from recipesiteapp.views import index

urlpatterns = [
    path('', index, name='index'),
]