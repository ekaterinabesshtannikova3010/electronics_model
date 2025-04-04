from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='ivanov@gmail.com',
            first_name='Ivan',
            last_name='Ivanov',
            is_staff=True,
            is_superuser=True
        )

        user.set_password('admin')
        user.save()
