from django.shortcuts import render

from .models import Producto

def listar(request):
	template_name = "productos/listar.html"
	# productos = Producto.objects.get(nombre="Nombre") -- filter(nombre="Nombre").order_by("-id")

	ctx = {
		"nombre_usuario": "Lucas",
		"lista_productos": Producto.objects.all()
	}
	
	return render(request, template_name, ctx)
