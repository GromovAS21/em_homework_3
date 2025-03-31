"""Команда для создания суперпользователя."""

import os

import django
from django.contrib.auth.models import User
from django.core.management import BaseCommand


class Command(BaseCommand):
    """Команда для создания суперпользователя."""

    def handle(self, *args, **options) -> None:
        """Создание суперпользователя.

        Args:
            *args: позиционные аргументы
            **options: ключевые аргументы

        Exceptions:
            django.db.utils.IntegrityError: если суперпользователь уже существует
            Exception: если произошла ошибка

        Returns:
            None
        """
        try:
            superuser = User.objects.create_superuser(
                username=os.getenv("SUPERUSER_LOGIN"),
            )
            superuser.set_password(os.getenv("SUPERUSER_PASSWORD"))
            superuser.save()

        except django.db.utils.IntegrityError:
            self.stdout.write(self.style.ERROR("SUPERUSER ALREADY CREATED"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(e))
        else:
            self.stdout.write(self.style.SUCCESS("SUPERUSER CREATE SUCCESS"))
