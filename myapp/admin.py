from django.contrib import admin
from .models import User, Product, Order

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'direction', 'date']
    readonly_fields = ['date']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name']
            }
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'fields': ['email', 'direction', 'date']
            }
        )
    ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'description', 'sum', 'date', 'image']
    readonly_fields = ['date']
    fieldsets = [
                    (
                        None,
                        {
                            'classes': ['wide'],
                            'fields': ['name'],
                        },
                    ),
                    (
                        'Подробности',
                        {
                            'classes': ['collapse'],
                            'description': 'Категория товара и его подробное описание',
                            'fields': ['price', 'description', 'image'],
                        },
                    ),
                    (
                        'Дата регистрации',
                        {
                            'classes': ['wide'],
                            'fields': ['date']
                        }
                    )
        ]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'date_ordered', 'total_price']
    readonly_fields = ['date_ordered']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['customer', 'date_ordered']
            }
        ),
        (
            'Заказ',
            {
                'classes': ['collapse'],
                'fields': ['products']
            }
        ),
        (
            'Цена',
            {
                'classes': ['wide'],
                'fields': ['total_price']
            }
        ),

    ]