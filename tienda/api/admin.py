from django.contrib import admin

# Register your models here.
from .models import Producto

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'precio', 'imagen', 'estado')

admin.site.register(Producto, ProductoAdmin)