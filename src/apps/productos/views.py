from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins     import LoginRequiredMixin
from django.shortcuts               import render
from django.urls                    import reverse_lazy
from django.views.generic           import ListView, CreateView

from .forms  import ProductoForm
from .models import Producto
"""
@login_required
def listar(request):
	template_name = "productos/listar.html"
	# productos = Producto.objects.get(nombre="Nombre") -- filter(nombre="Nombre").order_by("-id")

	ctx = {
		"nombre_usuario": "Lucas",
		"lista_productos": Producto.objects.all()
	}
	
	return render(request, template_name, ctx)


"""
class Listar(LoginRequiredMixin, ListView):
	template_name = "productos/listar.html"
	model = Producto
	context_object_name = 'lista_productos'
	paginate_by = 10

	def get_queryset(self):
		return Producto.objects.filter(activo=True).order_by("nombre")


# ======================================================
# 					Vistas para Admin
# ======================================================
class ListarAdmin(LoginRequiredMixin, ListView):
	template_name = "productos/admin/listar.html"
	model = Producto
	context_object_name = 'lista_productos'
	paginate_by = 10

	def get_queryset(self):
		return Producto.objects.all().order_by("id")

class Crear(LoginRequiredMixin, CreateView):
	template_name = "productos/admin/nuevo.html"
	model = Producto
	form_class = ProductoForm

	def get_success_url(self, **kwargs):
		return reverse_lazy("productos:admin_listar")