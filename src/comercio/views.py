from django.shortcuts          import render
from django.views.generic.base import TemplateView

from apps.productos.models import Producto

# Vista basa en funcion
"""
def inicio(request):
	template_name = "index.html"
	ultimos_productos = Producto.objects.all().order_by('-id')[:2]

	ctx = {
		'ultimos_productos': ultimos_productos
	}
	return render(request, template_name, ctx)
"""

# Vista basa en clases
class Inicio(TemplateView):
	template_name = "index.html"

	def get_context_data(self, **kwargs):
		context = super(Inicio, self).get_context_data(**kwargs)
		context["ultimos_productos"] = Producto.objects.all().order_by('-id')[:2]
		return context