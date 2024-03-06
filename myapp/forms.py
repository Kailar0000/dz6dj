from django.forms import ModelForm
from .models import Product


class NewProductForm(ModelForm):

    class Meta:
        model = Product
        exclude = ['deleted']