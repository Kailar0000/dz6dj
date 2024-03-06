from django.views.generic import TemplateView
from .models import Order, Product
from .forms import NewProductForm
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, reverse
from datetime import datetime, timedelta


def client_orders(request: HttpResponse, customer_id: int):
    orders = Order.objects.filter(customer__id=customer_id)
    return render(request, 'shopapp/client_orders.html',
                  context={'orders': orders, 'customer_id': customer_id})


class ClientProductsReport(TemplateView):
    template_name = 'shopapp/client_product_report.html'
    allowed_range_names = {
        'day': 1,
        'week': 7,
        'month': 30,
        'year': 365
    }

    def get_products(self, customer_id: int, days: int):
        products_info = {}
        orders_list = []
        orders = Order.objects.filter(customer__id=customer_id,
                                           registration_date__gte=datetime.now()-timedelta(days=days))
        for order in orders:
            orders_list.append(order.pk)
            for product in order.products.all():
                if product.name in products_info:
                    products_info[product.name] += 1
                else:
                    products_info[product.name] = 1
        return orders_list, products_info

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'range' not in context:
            context['range'] = 7
        elif context['range'].isdigit():
            context['range'] = int(context['range'])
        elif context['range'] in self.allowed_range_names:
            context['range_name'] = context['range']
            context['range'] = self.allowed_range_names[context['range']]
        else:
            raise Http404
        context['orders_list'], context['products_info'] = self.get_products(context['client_id'], context['range'])
        return context


def product_info(request, product_id):
    product = Product.objects.filter(pk=product_id).first()
    print(product)
    return render(request, 'shopapp/product_info.html',
                  context={'product': product, 'product_id': product_id})


def new_product(request):
    if request.method == 'POST':
        form = NewProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            return redirect(reverse('product_info', args=[product.pk]))
    else:
        form = NewProductForm()
    return render(request, 'shopapp/create_product.html', context={'form': form})
