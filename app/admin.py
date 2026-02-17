from django.contrib import admin
from .models import Topping, Pizza, Proveedor
# Register your models here.
admin.site.register(Topping)
admin.site.register(Pizza)
admin.site.register(Proveedor)