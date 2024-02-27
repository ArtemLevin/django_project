import json
from random import choice
from django.core.management.base import BaseCommand
from faker import Faker
from recipes.models import Recipe, User

fake = Faker("ru_RU")


class Command(BaseCommand):
    help = "Creates a fake recipe"

    def handle(self, *args, **kwargs):
        with open('recipes.txt', 'r', encoding='utf-8') as f:
            data = json.load(f)


        users_list = User.objects.all()

        for i in range(len(data)):
            dish = choice(list(data))
            recipe = Recipe.objects.create(
                name=dish['название'],
                description=dish['описание'],
                ingredients=dish['ингредиенты'],
                cooking_process=' '.join(dish['шаги']),
                author=choice(users_list),
                published_date=fake.date_time_this_year(),
                cooking_time=fake.random_int(min=1, max=10),
                amount_of_servings=fake.random_int(min=1, max=5),
                likes=fake.random_int(min=1, max=5),
                calories=fake.random_int(min=100, max=500),

            )
            recipe.save()

            self.stdout.write(f"Создан рецепт {recipe.name}")
