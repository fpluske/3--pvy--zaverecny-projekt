from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Create the demo superuser for the electronics shop.'

    def handle(self, *args, **options):
        user_model = get_user_model()
        username = 'admin'
        email = 'admin@elektrotrh.local'
        password = 'Admin12345!'

        user, created = user_model.objects.get_or_create(
            username=username,
            defaults={'email': email},
        )

        if created:
            user.is_staff = True
            user.is_superuser = True
            user.set_password(password)
            user.save()
            self.stdout.write(self.style.SUCCESS('Demo superuser created: admin / Admin12345!'))
            return

        if not user.is_superuser:
            user.is_staff = True
            user.is_superuser = True
            user.email = email
            user.set_password(password)
            user.save()
            self.stdout.write(self.style.SUCCESS('Existing user upgraded to demo superuser: admin / Admin12345!'))
            return

        self.stdout.write(self.style.WARNING('Demo superuser already exists.'))