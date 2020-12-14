from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from authapp.models import UserProfile


class Command(BaseCommand):
    def handle(self, *args, **options):
        # request.user.userprofile.age
        # request.user.userprofile.about
        for user in User.objects.filter(userprofile__isnull=True):
            UserProfile.objects.create(user=user)
            print(user)
