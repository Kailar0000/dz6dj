from django.core.management.base import BaseCommand
from dz6.myapp.models import Product


class Command(BaseCommand):
    help = "Print existing Product objects with id"

    def handle(self, *args, **options):
        for product in Product.objects.all():
            self.stdout.write(f"{product.id}. {product}")