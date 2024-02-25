import datetime

from django import forms
from . import models


class RecipeForm(forms.ModelForm):
    photo = forms.ImageField(required=False, widget=forms.FileInput())

    class Meta:
        model = models.Recipes
        fields = ['title', 'description', 'steps_cooking', 'photo', 'time_for_cooking', 'author']


class UpdateRecipeForm(forms.ModelForm):
    title = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    steps_cooking = forms.CharField(widget=forms.Textarea)
    time_for_cooking = forms.CharField(max_length=10)
    photo = forms.ImageField(required=False, widget=forms.FileInput())

    class Meta:
        model = models.Recipes
        fields = ['author']
