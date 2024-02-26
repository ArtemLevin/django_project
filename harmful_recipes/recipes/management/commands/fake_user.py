from random import choice
from django.core.management.base import BaseCommand
from faker import Faker
from recipes.models import User

fake = Faker("ru_RU")
class Command(BaseCommand):
    help = "Creates a fake user"

    def handle(self, *args, **kwargs):
        for i in range(10):
            user = User(
                name=fake.name(),
                email=fake.email(),
                password=fake.password(),
                age=fake.random_int(min=18, max=100),
                status=choice(["любитель", "дилетант", "только учусь", "уже умею", "профессионал"]),
                is_active=choice([True, False]),
                last_login=fake.date_time_this_month(),
                first_login=fake.date_time_this_year(),
            )
            user.save()

            self.stdout.write(f"Создан пользователь {user.name}")
