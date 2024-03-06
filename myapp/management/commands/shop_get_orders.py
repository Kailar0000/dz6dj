from django.core.management.base import BaseCommand
from dz6.myapp.models import Order


class Command(BaseCommand):
    help = "Print existing Order objects with id"

    def handle(self, *args, **options):
        for order in Order.objects.all():
            self.stdout.write(f"{order.id}. {order}")