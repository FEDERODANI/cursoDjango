from django.contrib import admin

from .models import Producto, Categoria, Tag

class ProductoAdmin(admin.ModelAdmin):
	list_display = ["id","nombre", "precio", "cantidad", "activo", "categoria"]

admin.site.register(Producto, ProductoAdmin)

class CategoriaAdmin(admin.ModelAdmin):
	list_display = ["id","nombre"]

admin.site.register(Categoria, CategoriaAdmin)

class TagAdmin(admin.ModelAdmin):
	list_display = ["id","nombre"]

admin.site.register(Tag, TagAdmin)