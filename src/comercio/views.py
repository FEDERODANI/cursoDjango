from django.shortcuts import render

from apps.productos.models import Producto

def inicio(request):
	template_name = "index.html"
	ultimos_productos = Producto.objects.all().order_by('-id')[:2]

	ctx = {
		'ultimos_productos': ultimos_productos
	}
	return render(request, template_name, ctx)

def login(request):
	template_name = "login.html"

	ctx = {

	}
	return render(request, template_name, ctx)