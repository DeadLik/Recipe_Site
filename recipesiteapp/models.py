from django.db import models
import users.models


class Recipes(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    steps_cooking = models.TextField()
    time_for_cooking = models.CharField(max_length=10, default=None)
    photo = models.ImageField(default=None)
    author = models.ForeignKey(users.models.User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'
