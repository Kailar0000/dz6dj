from django.core.management.base import BaseCommand
from dz6.myapp.models import User


class Command(BaseCommand):
    help = "Print existing Client objects with id"

    def handle(self, *args, **options):
        for client in User.objects.all():
            self.stdout.write(f"{client.id}. {client}")