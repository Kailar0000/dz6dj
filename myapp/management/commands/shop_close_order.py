from django.core.management.base import BaseCommand, CommandError
from dz6.myapp.models import Order
from django.utils import timezone


class Command(BaseCommand):
    help = "Update Order by set applied_date to now"

    def add_arguments(self, parser):
        parser.add_argument('order_id', type=int, help='id')

    def handle(self, *args, **options):
        order_id = options.get('order_id')
        order = Order.objects.filter(pk=order_id).first()
        if order:
            if order.applied_date:
                raise CommandError(f"Order already closed")
            order.applied_date = timezone.now()
            order.save()
        else:
            raise CommandError(f"Unable to find Product by id '{order_id}'")