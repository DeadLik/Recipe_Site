from django.core.management.base import BaseCommand
from django.utils import lorem_ipsum
from random import randint, choice

import users.models
from recipesiteapp.models import Recipes


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        user = users.models.User.objects.all()
        for i in range(0, 10):
            recipe = Recipes(title=f'Рецепт_{i}',
                             description=lorem_ipsum.paragraphs(4),
                             steps_cooking=lorem_ipsum.paragraphs(2),
                             time_for_cooking=f'{randint(1, 10)} мин',
                             author=choice(user),
                             )
            recipe.save()
        self.stdout.write('Рецепты добавлены')
